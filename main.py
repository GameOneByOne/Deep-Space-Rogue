import asyncio
import json
import time
from collections import deque
from threading import Lock
from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from GameEngine import GameEngine

app = FastAPI(title="Deep Space Rogue API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

g_engineByClient: dict[str, GameEngine] = {}
g_engineLock = Lock()
g_eventQueues: dict[str, deque] = {}
g_eventSignals: dict[str, asyncio.Event] = {}
g_eventLock = Lock()
g_loop: asyncio.AbstractEventLoop | None = None
SSE_KEEPALIVE_SECONDS = 15

@app.on_event("startup")
async def _on_startup():
    global g_loop
    g_loop = asyncio.get_running_loop()

def _get_client_id(clientIdHeader: str | None, clientIdQuery: str | None) -> str:
    if clientIdHeader:
        return clientIdHeader
    if clientIdQuery:
        return clientIdQuery
    raise HTTPException(status_code=400, detail="Missing client id (use X-Client-Id header or clientId query)")

def _get_event_queue(clientId: str) -> deque:
    with g_eventLock:
        q = g_eventQueues.get(clientId)
        if q is None:
            q = deque()
            g_eventQueues[clientId] = q
        return q

def _get_event_signal(clientId: str) -> asyncio.Event:
    with g_eventLock:
        signal = g_eventSignals.get(clientId)
        if signal is None:
            signal = asyncio.Event()
            g_eventSignals[clientId] = signal
        return signal

def _push_event(clientId: str, payload: dict) -> None:
    with g_eventLock:
        q = g_eventQueues.get(clientId)
        if q is None:
            q = deque()
            g_eventQueues[clientId] = q
        q.append(payload)
        signal = g_eventSignals.get(clientId)
    if signal is not None and g_loop is not None:
        g_loop.call_soon_threadsafe(signal.set)

def GetEngine(
    clientIdHeader: str | None = Header(default=None, alias="X-Client-Id"),
    clientId: str | None = Query(default=None),
) -> GameEngine:
    clientId = _get_client_id(clientIdHeader, clientId)

    with g_engineLock:
        engine = g_engineByClient.get(clientId)
        if engine is None:
            engine = GameEngine()
            g_engineByClient[clientId] = engine
        return engine

@app.get("/state")
def GetState(engine: GameEngine = Depends(GetEngine)):
    engine.Tick()
    mainInfos, buildings, resources, professions, researchInfos = engine.Show()
    return {
        "main": mainInfos,
        "buildings": buildings,
        "resources": resources,
        "professions": professions,
        "research": researchInfos,
    }

@app.post("/build/{buildingId}")
def build(buildingId: str, engine: GameEngine = Depends(GetEngine)):
    engine.Tick()
    engine.Build(buildingId)
    return {"result": True}

@app.post("/research/{researchId}")
def research(researchId: str, engine: GameEngine = Depends(GetEngine)):
    engine.Tick()
    engine.Research(researchId)
    return {"result": True}

@app.post("/dispatch/{fromProfessionId}/{toProfessionId}")
def dispatch(fromProfessionId: str, toProfessionId: str, engine: GameEngine = Depends(GetEngine)):
    engine.Tick()
    engine.Dispatch(fromProfessionId, toProfessionId)
    return {"result": True}

@app.post("/undispatch/{fromProfessionId}/{toProfessionId}")
def undispatch(fromProfessionId: str, toProfessionId: str, engine: GameEngine = Depends(GetEngine)):
    engine.Tick()
    engine.Dispatch(fromProfessionId, toProfessionId)
    return {"result": True}

@app.get("/events")
async def events(request: Request, clientId: str = Query(...)):
    signal = _get_event_signal(clientId)

    async def event_stream():
        hello = {"type": "hello", "clientId": clientId}
        yield f"data: {json.dumps(hello, ensure_ascii=False)}\n\n"
        last_keepalive = time.monotonic()
        try:
            while True:
                if await request.is_disconnected():
                    break
                payload = None
                with g_eventLock:
                    q = g_eventQueues.get(clientId)
                    if q:
                        payload = q.popleft()
                if payload is not None:
                    yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
                    continue
                try:
                    waiters = [asyncio.create_task(signal.wait())]
                    done, pending = await asyncio.wait(
                        waiters,
                        timeout=SSE_KEEPALIVE_SECONDS,
                        return_when=asyncio.FIRST_COMPLETED,
                    )
                    for task in pending:
                        task.cancel()
                    if signal.is_set():
                        signal.clear()
                except asyncio.TimeoutError:
                    now = time.monotonic()
                    if now - last_keepalive >= SSE_KEEPALIVE_SECONDS:
                        yield ": keep-alive\n\n"
                        last_keepalive = now
        except asyncio.CancelledError:
            return

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )

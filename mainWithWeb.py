from threading import Lock
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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

def GetEngine(clientId: str = Header(default=None, alias="X-Client-Id")) -> GameEngine:
    if not clientId:
        raise HTTPException(status_code=400, detail="Missing client id (use X-Client-Id header)")

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

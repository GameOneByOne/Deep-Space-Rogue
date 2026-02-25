from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameEffect import EffectExecutor


@dataclass(frozen=True)
class EventDef:
    """事件静态数据: 来自cfg, 不可在运行时修改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    weight: int = 0
    cooldown: int = 0
    prereqs: List[dict] = field(default_factory=list)
    effects: List[dict] = field(default_factory=list)

    @staticmethod
    def FromDict(data: dict) -> EventDef:
        return EventDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            weight = data.get("weight", 0),
            cooldown = data.get("cooldown", 0),
            prereqs = data.get("prereqs", []),
            effects = data.get("effects", [])
        )


@dataclass
class EventState:
    """运行时事件状态（可存档）"""
    eventDef: EventDef = field(default_factory=EventDef)
    unlocked: bool = False

    @staticmethod
    def FromDict(data: dict):
        state = EventState()
        state.eventDef = EventDef.FromDict(data)
        state.unlocked = True if state.eventDef.defaultUnlock else False
        return state


class EventManager:
    """事件运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, EventState] = {}
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for eventInfo in cfgList:
            self.state[eventInfo["id"]] = EventState.FromDict(eventInfo)

    def Unlock(self, eventId: str):
        if eventId not in self.state:
            return
        self.state[eventId].unlocked = True
        return

    def IsUnlocked(self, eventId: str):
        if eventId not in self.state:
            return False
        return self.state[eventId].unlocked

    def Tick(self):
        return

    def GetFrontData(self):
        data = list()
        for eventState in self.state.values():
            if not eventState.unlocked:
                continue
            info = dict()
            info["id"] = eventState.eventDef.id
            info["name"] = eventState.eventDef.name
            info["desc"] = eventState.eventDef.desc
            info["weight"] = eventState.eventDef.weight
            info["cooldown"] = eventState.eventDef.cooldown
            info["prereqs"] = eventState.eventDef.prereqs
            info["effects"] = [str(EffectExecutor.FromDict(effect)) for effect in eventState.eventDef.effects]
            data.append(info)
        return data

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class ResourceDef:
    """资源数据类，用来表示一种资源，都是静态数据不可更改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    defaultCapacity: float = 0.0

    @staticmethod
    def FromDict(data: dict) -> ResourceDef :
        return ResourceDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            defaultCapacity = data.get("defaultCapacity", 0.0)
        )


@dataclass
class ResourceState:
    """运行时资源状态（可存档）"""
    resDef: ResourceDef = field(default_factory=ResourceDef)
    unlocked: bool = False
    amount: float = 0.0
    capacity: float = 0.0
    effectBy: Dict[str, list] = field(default_factory=dict)
    producedRate: float = 0.0

    @staticmethod
    def FromDict(data: dict) :
        state = ResourceState()
        state.resDef = ResourceDef.FromDict(data)
        state.unlocked = True if state.resDef.defaultUnlock else False
        state.capacity = state.resDef.defaultCapacity
        return state
    
    def UpdateValue() :
        return


class ResourceManager:
    """资源运行时管理器"""
    def __init__(self, cfgFilePath : str):
        self.state : Dict[str, ResourceState] = {}
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for resourceInfo in cfgList:
            self.state[resourceInfo["id"]] = ResourceState.FromDict(resourceInfo)

    def Unlock(self, resourceId: str) :
        self.state[resourceId].unlocked = True
        return

    def IsUnlocked(self, resourceId: str) :
        return self.state[resourceId].unlocked

    def GetCapacity(self, resourceId: str) :
        return

    def AddAmount(self, resourceId: str, delta: float) :
        self.state[resourceId].amount = min(self.state[resourceId].capacity, self.state[resourceId].amount + delta)
        return

    def ClampAmount(self, resourceId: str, delta: float) -> bool:
        self.state[resourceId].amount = max(0, self.state[resourceId].amount - delta)
        return

    def GetAmount(self, resourceId: str) :
        return self.state[resourceId].amount

    def IsEnough(self, resourceNeed: list) -> bool:
        for resource in resourceNeed :
            if self.state[resource["id"]].amount < resource["need"] :
                return False
        return True
    
    def ApplyEffect(self, fromEntityId: str, toEntityId: str, effect) :
        return

    def RevertEffect(self, fromEntityId: str, toEntityId: str, effect) :
        return

    def GetFrontData(self) :
        data = list()
        for resourceState in self.state.values() :
            if not resourceState.unlocked :
                continue
            info = dict()
            info["id"] = resourceState.resDef.id
            info["name"] = resourceState.resDef.name
            info["desc"] = resourceState.resDef.desc
            info["count"] = resourceState.amount
            info["limit"] = resourceState.capacity
            info["rate"] = resourceState.producedRate
            data.append(info)
        return data

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

    commonEffectBy: Dict[str, list] = field(default_factory=dict)
    producedRate: float = 0.0

    convertEffectBy: Dict[str, list] = field(default_factory=dict)
    convertInResources: Dict[str, int] = field(default_factory=dict)
    convertProducedRate: float = 0.0

    @staticmethod
    def FromDict(data: dict) :
        state = ResourceState()
        state.resDef = ResourceDef.FromDict(data)
        state.unlocked = True if state.resDef.defaultUnlock else False
        state.capacity = state.resDef.defaultCapacity
        return state

    def UpdateState(self) :
        self.producedRate = 0.0

        # 重新计算普通作用
        for effects in self.commonEffectBy.values() :
            for effect in effects :
                if effect["type"] == "produce" :
                    self.producedRate += effect.get("rate", 0)
                    continue

                if effect["type"] == "consume" :
                    self.producedRate -= effect.get("rate", 0)
                    continue

        # 重新计算转化作用
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
        return self.state[resourceId].capacity

    def AddAmount(self, resourceId: str, delta: float) :
        self.state[resourceId].amount = min(self.state[resourceId].capacity, self.state[resourceId].amount + delta)
        return

    def ClampAmount(self, resourceId: str, delta: float) -> bool:
        self.state[resourceId].amount = max(0, self.state[resourceId].amount - delta)
        return

    def ConvertAmount(self, inResources, outResource) :
        if not self.IsEnough(inResources) :
            return
        
        for res in inResources :
            self.ClampAmount(res["resourceId"], res["need"])
        self.AddAmount(outResource["resourceId"], outResource["amount"])
        return

    def GetAmount(self, resourceId: str) :
        return self.state[resourceId].amount

    def IsEnough(self, resourceNeed: list) -> bool:
        for resource in resourceNeed :
            if self.state[resource["id"]].amount < resource["need"] :
                return False
        return True

    def ApplyCommonEffect(self, fromEntityId: str, toEntityId: str, commonEffect) :
        if fromEntityId not in self.state[toEntityId].commonEffectBy:
            self.state[toEntityId].commonEffectBy[fromEntityId] = list()
        self.state[toEntityId].commonEffectBy[fromEntityId].append(commonEffect)
        self.state[toEntityId].UpdateState()
        return

    def RevertCommonEffect(self, fromEntityId: str, toEntityId: str, commonEffect) :
        self.state[toEntityId].commonEffectBy[fromEntityId].remove(commonEffect)
        self.state[toEntityId].UpdateState()
        return

    def ApplyConvertEffect(self, fromEntityId: str, toEntityId: str, convertEffect) :
        self.state[toEntityId].convertEffectBy[fromEntityId].append(convertEffect)
        self.state[toEntityId].UpdateState()
        return

    def RevertConvertEffect(self, fromEntityId: str, toEntityId: str, convertEffect) :
        self.state[toEntityId].convertEffectBy[fromEntityId].append(convertEffect)
        self.state[toEntityId].UpdateState()
        return
    
    def Tick(self) :
        for res in self.state.values() :
            if res.producedRate >= 0 :
                self.AddAmount(res.resDef.id, res.producedRate)
            else :
                self.ClampAmount(res.resDef.id, res.producedRate)
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

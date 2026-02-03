from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameUtils import EffectUtils


@dataclass(frozen=True)
class ProfessionDef:
    """职业数据类，用来表示一种职业，都是静态数据不可更改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    editable: bool = True
    tags: List[str] = field(default_factory=list)
    effects: List[dict] = field(default_factory=list)

    @staticmethod
    def FromDict(data: dict) :
        return ProfessionDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            editable = data.get("editable", True),
            tags = data.get("tags", []),
            effects = data.get("effects", [])
        )


@dataclass
class ProfessionState:
    """运行时职业状态（可存档）"""
    profDef: ProfessionDef = field(default_factory=ProfessionDef)
    unlocked: bool = False
    amount: int = 0
    limit: int = 0
    effectBy: Dict[str, list] = field(default_factory=dict)

    @staticmethod
    def FromDict(data: dict):
        state = ProfessionState()
        state.profDef = ProfessionDef.FromDict(data)
        state.unlocked = True if state.profDef.defaultUnlock else False
        return state

    def UpdateState(self) :
        oldLimit = self.limit
        self.limit = 0
        for effects in self.effectBy.values() :
            for effect in effects :
                if effect.get("type", "") == "addJobSlot" :
                    self.limit += effect.get("slots", 0)
                    continue

        if self.profDef.id != "P_IDLE" :
            return
        
        # 闲置人口需要单独算一下
        if self.limit > oldLimit :
            self.amount += (self.limit - oldLimit)
        return


class ProfessionManager:
    """职业运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, ProfessionState] = {}
        self.population = 0
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for professionInfo in cfgList:
            self.state[professionInfo["id"]] = ProfessionState.FromDict(professionInfo)

    def Unlock(self, professionId: str) :
        self.state[professionId].unlocked = True
        return

    def IsUnlocked(self, professionId: str) :
        return self.state[professionId].unlocked

    def GetDef(self, professionId: str) :
        return self.state[professionId].profDef

    def GetEffects(self, professionId: str) :
        return self.state[professionId].profDef.effects

    def ApplyEffect(self, fromEntityId: str, toEntityId: str, effect) :
        oldAmount = self.state[toEntityId].amount
        if fromEntityId not in self.state[toEntityId].effectBy :
            self.state[toEntityId].effectBy[fromEntityId] = list()
        self.state[toEntityId].effectBy[fromEntityId].append(effect)
        self.state[toEntityId].UpdateState()
        self.population = max(0, self.population + (self.state[toEntityId].amount - oldAmount))
        return

    def RevertEffect(self, fromEntityId: str, toEntityId: str, effect):
        oldAmount = self.state[toEntityId].amount
        self.state[toEntityId].effectBy[fromEntityId].remove(effect)
        self.state[toEntityId].UpdateState()
        self.population = max(0, self.population + (self.state[toEntityId].amount - oldAmount))
        return

    def GetFrontData(self) :
        data = list()
        for professionState in self.state.values() :
            if not professionState.unlocked :
                continue
            info = dict()
            info["id"] = professionState.profDef.id
            info["name"] = professionState.profDef.name
            info["desc"] = professionState.profDef.desc
            info["count"] = professionState.amount
            info["limit"] = professionState.limit
            info["canEdit"] = professionState.profDef.editable
            info["effects"] = [EffectUtils.GetEffectDesc(effect) for effect in professionState.profDef.effects]
            data.append(info)
        return data

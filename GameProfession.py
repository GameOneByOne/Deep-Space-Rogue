from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


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
        return

    def RevertEffect(self, fromEntityId: str, toEntityId: str, effect):
        return

    def AddPeople(self, professionId: str, count: int) :
        self.population += count
        self.state[professionId].amount += count
        return count

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
            info["canEdit"] = professionState.profDef.editable
            data.append(info)
        return data

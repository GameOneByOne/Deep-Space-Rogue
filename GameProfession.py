from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameUtils import Utils
from GameEffect import EffectExecutor, Effect, UnlockEffect, AddEffect, ClampEffect, AddLimitEffect


@dataclass(frozen=True)
class ProfessionDef:
    """职业数据类，用来表示一种职业，都是静态数据不可更改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    editable: bool = True
    effects: List[dict] = field(default_factory=list)

    @staticmethod
    def FromDict(data: dict) :
        return ProfessionDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            editable = data.get("editable", True),
            effects = data.get("effects", [])
        )


@dataclass
class ProfessionState:
    """运行时职业状态（可存档）"""
    profDef: ProfessionDef = field(default_factory=ProfessionDef)
    unlocked: bool = False
    amount: int = 0
    limit: int = 0

    @staticmethod
    def FromDict(data: dict):
        state = ProfessionState()
        state.profDef = ProfessionDef.FromDict(data)
        state.unlocked = True if state.profDef.defaultUnlock else False
        return state

    def UpdateState(self) :
        return


class ProfessionManager:
    """职业运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, ProfessionState] = {}
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for professionInfo in cfgList:
            self.state[professionInfo["id"]] = ProfessionState.FromDict(professionInfo)

    def Unlock(self, professionId: str) :
        if professionId not in self.state :
            return False
        self.state[professionId].unlocked = True
        return True

    def IsUnlocked(self, professionId: str) :
        if professionId not in self.state :
            return False
        return self.state[professionId].unlocked
    
    def canDispatch(self, fromProfessionId: str, toProfessionId: str) :
        if self.state[fromProfessionId].amount <= 0 :
            return False
        if self.state[toProfessionId].amount >= self.state[toProfessionId].limit :
            return False
        return True
    
    def Dispatch(self, fromProfessionId: str, toProfessionId: str) :
        self.state[fromProfessionId].amount -= 1
        self.state[toProfessionId].amount += 1
        return [EffectExecutor.FromDict(x).GetOppositeEffect() for x in self.state[fromProfessionId].profDef.effects], \
            [EffectExecutor.FromDict(x) for x in self.state[toProfessionId].profDef.effects]

    def ApplyEffect(self, effect: Effect) :
        if isinstance(effect, UnlockEffect) :
            self.Unlock(effect.toId)
            return
        elif isinstance(effect, AddEffect) :
            self.state[effect.toId].amount += effect.count
            return [EffectExecutor.FromDict(x) for x in self.state[effect.toId].profDef.effects] * effect.count
        elif isinstance(effect, ClampEffect) :
            self.state[effect.toId].amount -= effect.count
            return [EffectExecutor.FromDict(x).GetOppositeEffect() for x in self.state[effect.toId].profDef.effects] * effect.count
        elif isinstance(effect, AddLimitEffect) :
            self.state[effect.toId].limit += effect.count
            return

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
            info["effectsDesc"] = [Utils.GetEffectDesc(effect) for effect in professionState.profDef.effects]
            data.append(info)
        return data

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameUtils import Utils


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
                e_type = effect.get("type", "")
                if e_type == "add" and effect.get("target", "") == "profession" :
                    self.limit += effect.get("count", 0)
                    continue
                if e_type == "clamp" and effect.get("target", "") == "profession" :
                    self.limit -= effect.get("count", 0)
                    continue

        if self.profDef.id != "P_IDLE" :
            if self.limit < 0:
                self.limit = 0
            return
        
        if self.limit < 0:
            self.limit = 0
        
        # 闲置人口需要单独算一下
        if self.limit > oldLimit :
            self.amount += (self.limit - oldLimit)
        elif self.amount > self.limit :
            self.amount = self.limit
        return


class ProfessionManager:
    """职业运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, ProfessionState] = {}
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for professionInfo in cfgList:
            self.state[professionInfo["id"]] = ProfessionState.FromDict(professionInfo)

    def Unlock(self, professionId: str) :
        self.state[professionId].unlocked = True
        return

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
        return self.state[fromProfessionId].profDef.effects, self.state[toProfessionId].profDef.effects

    def GetDef(self, professionId: str) :
        return self.state[professionId].profDef

    def GetEffects(self, professionId: str) :
        return self.state[professionId].profDef.effects

    def GetRuntimeEffects(self, professionId: str) :
        effects = list()
        pState = self.state[professionId]
        for effectList in pState.effectBy.values() :
            for effect in effectList :
                effects.append(effect)
        return effects

    def GetAllEffects(self, professionId: str) :
        effects = list()
        effects.extend(self.GetEffects(professionId))
        effects.extend(self.GetRuntimeEffects(professionId))
        return effects

    def ApplyEffect(self, fromEntityId: str, toEntityId: str, effect) :
        if fromEntityId not in self.state[toEntityId].effectBy :
            self.state[toEntityId].effectBy[fromEntityId] = list()
        self.state[toEntityId].effectBy[fromEntityId].append(effect)
        self.state[toEntityId].UpdateState()
        return

    def RevertEffect(self, fromEntityId: str, toEntityId: str, effect):
        self.state[toEntityId].effectBy[fromEntityId].remove(effect)
        self.state[toEntityId].UpdateState()
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

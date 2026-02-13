from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameEffect import EffectExecutor


@dataclass(frozen=True)
class ResearchDef:
    """研究静态数据: 来自cfg, 不可在运行时修改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    cost: List[dict] = field(default_factory=list)
    prereqs: List[dict] = field(default_factory=list)
    effects: List[dict] = field(default_factory=list)

    @staticmethod
    def FromDict(data: dict) -> ResearchDef:
        return ResearchDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            cost = data.get("cost", []),
            prereqs = data.get("prereqs", []),
            effects = data.get("effects", []),
        )


@dataclass
class ResearchState:
    """运行时研究状态（可存档）"""
    researchDef: ResearchDef = field(default_factory=ResearchDef)
    unlocked: bool = False
    finished: bool = False
    effectBy: Dict[str, list] = field(default_factory=dict)

    @staticmethod
    def FromDict(data: dict):
        state = ResearchState()
        state.researchDef = ResearchDef.FromDict(data)
        state.unlocked = True if state.researchDef.defaultUnlock else False
        state.finished = False
        return state


class ResearchManager:
    """研究运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, ResearchState] = {}
        rawCfg = json.loads(Path(cfgFilePath).read_text("utf-8"))
        cfgList = rawCfg if isinstance(rawCfg, list) else []
        for researchInfo in cfgList:
            self.state[researchInfo["id"]] = ResearchState.FromDict(researchInfo)

    def Unlock(self, researchId: str):
        if researchId not in self.state:
            return
        self.state[researchId].unlocked = True
        return

    def IsUnlocked(self, researchId: str):
        if researchId not in self.state:
            return False
        return self.state[researchId].unlocked

    def IsFinished(self, researchId: str):
        if researchId not in self.state:
            return False
        return self.state[researchId].finished

    def GetResearchCost(self, researchId: str):
        if researchId not in self.state:
            return []
        return self.state[researchId].researchDef.cost

    def Finish(self, researchId: str):
        if researchId not in self.state:
            return []
        rState = self.state[researchId]
        if not rState.unlocked or rState.finished:
            return []
        rState.finished = True
        return [EffectExecutor.FromDict(x) for x in rState.researchDef.effects]

    def GetDef(self, researchId: str) -> ResearchDef:
        return self.state[researchId].researchDef

    def GetFrontData(self):
        data = list()
        for researchState in self.state.values():
            if not researchState.unlocked:
                continue

            info = dict()
            info["id"] = researchState.researchDef.id
            info["name"] = researchState.researchDef.name
            info["desc"] = researchState.researchDef.desc
            info["cost"] = researchState.researchDef.cost
            info["finished"] = researchState.finished
            info["unlocked"] = researchState.unlocked
            info["costDesc"] = [EffectExecutor.GetCostDesc(cost) for cost in researchState.researchDef.cost]
            info["effectsDesc"] = [str(EffectExecutor.FromDict(effect)) for effect in researchState.researchDef.effects]
            data.append(info)
        return data

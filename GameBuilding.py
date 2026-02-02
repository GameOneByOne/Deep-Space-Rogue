from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from GameUtils import EffectUtils


@dataclass(frozen=True)
class BuildingDef:
    """建筑静态数据: 来自cfg, 不可在运行时修改"""
    id: str = ""
    name: str = ""
    desc: str = ""
    defaultUnlock: bool = False
    onlyClick: bool = False

    tags: List[str] = field(default_factory=list)
    cost: List[dict] = field(default_factory=list)
    prereqs: List[dict] = field(default_factory=list)
    effects: List[dict] = field(default_factory=list)

    @staticmethod
    def FromDict(data: dict) -> BuildingDef:
        return BuildingDef(
            id = data.get("id", ""),
            name = data.get("name", ""),
            desc = data.get("desc", ""),
            defaultUnlock = data.get("defaultUnlock", False),
            onlyClick = data.get("onlyClick", False),
            tags = data.get("tags", []),
            cost = data.get("cost", []),
            prereqs = data.get("prereqs", []),
            effects = data.get("effects", []),
        )


@dataclass
class BuildingState:
    """运行时建筑状态（可存档）"""
    buildingDef: BuildingDef = field(default_factory=BuildingDef)
    unlocked: bool = False
    ownedCount: int = 0
    effectBy: Dict[str, list] = field(default_factory=dict)

    @staticmethod
    def FromDict(data: dict) :
        state = BuildingState()
        state.buildingDef = BuildingDef.FromDict(data)
        state.unlocked = True if state.buildingDef.defaultUnlock else False
        state.ownedCount = 0
        return state


class BuildingManager:
    """建筑运行时管理器"""
    def __init__(self, cfgFilePath: str):
        self.state: Dict[str, BuildingState] = {}
        cfgList = json.loads(Path(cfgFilePath).read_text("utf-8"))
        for buildingInfo in cfgList:
            self.state[buildingInfo["id"]] = BuildingState.FromDict(buildingInfo)

    def Unlock(self, buildingId: str):
        self.state[buildingId].unlocked = True
        return

    def IsUnlocked(self, buildingId: str):
        return self.state[buildingId].unlocked

    def GetOwnedCount(self, buildingId: str):
        return self.state[buildingId].ownedCount
    
    def GetBuildingPrereqs(self, buildingId: str) :
        return self.state[buildingId].buildingDef.prereqs

    def GetBuildingCost(self, buildingId: str) :
        return self.state[buildingId].buildingDef.cost

    def Build(self, buildingId: str) :
        bState = self.state[buildingId]
        if not bState.buildingDef.onlyClick:
            bState.ownedCount += 1
        return bState.buildingDef.effects

    def GetDef(self, buildingId: str) -> BuildingDef:
        return self.state[buildingId].buildingDef

    def GetFrontData(self) :
        data = list()
        for buildingState in self.state.values() :
            if not buildingState.unlocked :
                continue

            info = dict()
            info["id"] = buildingState.buildingDef.id
            info["name"] = buildingState.buildingDef.name
            info["desc"] = buildingState.buildingDef.desc
            info["cost"] = buildingState.buildingDef.cost
            info["count"] = buildingState.ownedCount
            info["unlocked"] = buildingState.unlocked
            info["effects"] = [EffectUtils.GetEffectDesc(effect) for effect in buildingState.buildingDef.effects]
            data.append(info)
        return data

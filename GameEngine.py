import time
from GameBuilding import BuildingManager
from GameResource import ResourceManager
from GameProfession import ProfessionManager
from GameResearch import ResearchManager
from GameEffect import EffectExecutor
from GameUtils import Utils


BUILDING_DATA_PATH = "data/building.dat"
RESOURCE_DATA_PATH = "data/resource.dat"
PROFESSION_DATA_PATH = "data/profession.dat"
RESEARCH_DATA_PATH = "data/research.dat"


class GameEngine :
    def __init__(self) :
        # 初始化建筑数据
        self.buildingManager =  BuildingManager(BUILDING_DATA_PATH)
        for bState in self.buildingManager.state.values() :
            Utils.AddEntityToNameMap(bState.buildingDef.id, bState.buildingDef.name)

        # 初始化资源数据
        self.resourceManager = ResourceManager(RESOURCE_DATA_PATH)
        for rState in self.resourceManager.state.values() :
            Utils.AddEntityToNameMap(rState.resDef.id, rState.resDef.name)

        # 初始化人力职业数据
        self.professionManager = ProfessionManager(PROFESSION_DATA_PATH)
        for pState in self.professionManager.state.values() :
            Utils.AddEntityToNameMap(pState.profDef.id, pState.profDef.name)

        # 初始化研究数据
        self.researcheManager = ResearchManager(RESEARCH_DATA_PATH)
        for rState in self.researcheManager.state.values() :
            Utils.AddEntityToNameMap(rState.researchDef.id, rState.researchDef.name)

        self.effectExecutor = EffectExecutor(
            self.buildingManager,
            self.resourceManager,
            self.professionManager,
            self.researcheManager,
        )
        
        # 记录上次更新时间
        self.updateTime = time.time()

    def Build(self, buildingId : str) :
        # 非法入参或者建筑未解锁直接返回
        if not self.buildingManager.IsUnlocked(buildingId) :
            return

        # 不够资源消耗直接返回
        cost = self.buildingManager.GetBuildingCost(buildingId)
        if not self.resourceManager.IsEnough(cost) :
            return

        # 建筑消耗建造资源
        for item in cost :
            self.resourceManager.Clamp(item["id"], item["need"])

        # 应用建筑效果
        effects = self.buildingManager.Build(buildingId)
        self.ApplyEffects(buildingId, effects)
        return

    def Research(self, researchId: str) :
        # 研究未解锁或已完成，直接返回
        if not self.researcheManager.IsUnlocked(researchId) or self.researcheManager.IsFinished(researchId):
            return

        # 不满足研究前置直接返回
        prereqs = self.researcheManager.GetResearchPrereqs(researchId)
        if not self.CheckPrereqs(prereqs) :
            return

        # 不够研究资源直接返回
        cost = self.researcheManager.GetResearchCost(researchId)
        if not self.resourceManager.IsEnough(cost) :
            return

        # 消耗研究资源并完成研究
        for item in cost :
            self.resourceManager.Clamp(item["id"], item["need"])

        effects = self.researcheManager.Finish(researchId)
        self.ApplyEffects(researchId, effects)
        return True
    
    def Dispatch(self, fromProfessionId : str, toProfessionId : str) :
        # 未解锁的职业直接返回
        if not self.professionManager.IsUnlocked(toProfessionId) :
            return

        # 判断是否能进行分配
        if not self.professionManager.canDispatch(fromProfessionId, toProfessionId) :
            return

        # 进行职业分配
        revertEffects, newEffects = self.professionManager.Dispatch(fromProfessionId, toProfessionId)
        self.RevertEffects(fromProfessionId, revertEffects)
        self.ApplyEffects(toProfessionId, newEffects)
        return True
   
    def GetFrontData(self) :
        data = dict()
        return data

    def Tick(self) :
        currentTime = int(time.time())
        timeDelta = currentTime - self.updateTime
        self.updateTime = currentTime
        self.resourceManager.Tick(timeDelta)
        return

    def Show(self) :
        resourceInfos = {info["id"]: info for info in self.resourceManager.GetFrontData()}
        buildingInfos = {info["id"]: info for info in self.buildingManager.GetFrontData() }
        professionInfos = {info["id"]: info for info in self.professionManager.GetFrontData()}
        researchInfos = {info["id"]: info for info in self.researcheManager.GetFrontData()}
        mainInfos = self.GetFrontData()
        return mainInfos, buildingInfos, resourceInfos, professionInfos, researchInfos

    def ApplyEffects(self, fromEntifyId : str, effects: list) :
        for effect in effects :
            effectExec = self.effectExecutor.FromDict(fromEntifyId, effect)
            effectExec.Apply()
        return
    
    def RevertEffects(self, fromEntifyId : str, effects: list) :
        for effect in effects :
            effectExec = self.effectExecutor.FromDict(fromEntifyId, effect)
            effectExec.Revert()
        return

    def CheckPrereqs(self, prereqs: list) :
        for prereq in prereqs :
            pType = prereq.get("type", "")
            if pType == "hasBuilding" :
                if self.buildingManager.GetOwnedCount(prereq.get("id", "")) <= 0 :
                    return False
                continue
            if pType == "hasResearch" :
                if not self.researcheManager.IsFinished(prereq.get("id", "")) :
                    return False
                continue
        return True

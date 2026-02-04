from GameBuilding import BuildingManager
from GameResource import ResourceManager
from GameProfession import ProfessionManager
from GameResearch import ResearchManager
from GameUtils import EffectUtils


BUILDING_DATA_PATH = "data/building.cfg"
RESOURCE_DATA_PATH = "data/resource.cfg"
PROFESSION_DATA_PATH = "data/profession.cfg"
RESEARCH_DATA_PATH = "data/research.cfg"


class GameEngine :
    def __init__(self) :
        # 初始化建筑数据
        self.buildings =  BuildingManager(BUILDING_DATA_PATH)
        for bState in self.buildings.state.values() :
            EffectUtils.AddEntityToNameMap(bState.buildingDef.id, bState.buildingDef.name)

        # 初始化资源数据
        self.resourceManager = ResourceManager(RESOURCE_DATA_PATH)
        for rState in self.resourceManager.state.values() :
            EffectUtils.AddEntityToNameMap(rState.resDef.id, rState.resDef.name)

        # 初始化人力职业数据
        self.professionManager = ProfessionManager(PROFESSION_DATA_PATH)
        for pState in self.professionManager.state.values() :
            EffectUtils.AddEntityToNameMap(pState.profDef.id, pState.profDef.name)

        # 初始化研究数据
        self.researcheManager = ResearchManager(RESEARCH_DATA_PATH)
        for rState in self.researcheManager.state.values() :
            EffectUtils.AddEntityToNameMap(rState.researchDef.id, rState.researchDef.name)

    def Build(self, buildingId : str) :
        # 建筑未解锁直接返回
        if not self.buildings.IsUnlocked(buildingId) :
            return

        # 不够资源消耗直接返回
        cost = self.buildings.GetBuildingCost(buildingId)
        if not self.resourceManager.IsEnough(cost) :
            return

        # 建筑消耗建造资源
        for item in cost :
            self.resourceManager.ClampAmount(item["id"], item["need"])

        # 应用建筑效果
        effects = self.buildings.Build(buildingId)
        self.ApplyEffects(buildingId, effects)
        return True

    def Research(self, researchId: str) :
        # 研究未解锁或已完成，直接返回
        if not self.researcheManager.IsUnlocked(researchId) :
            return
        if self.researcheManager.IsFinished(researchId) :
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
            self.resourceManager.ClampAmount(item["id"], item["need"])

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
        # 资源更新
        self.resourceManager.Tick()
        return

    def Show(self) :
        resourceInfos = {info["id"]: info for info in self.resourceManager.GetFrontData()}

        buildingInfos = {}
        for info in self.buildings.GetFrontData() :
            buildingId = info["id"]
            bDef = self.buildings.GetDef(buildingId)
            info["canBuild"] = self.resourceManager.IsEnough(bDef.cost)
            buildingInfos[buildingId] = info

        professionInfos = {info["id"]: info for info in self.professionManager.GetFrontData()}
        researchInfos = {info["id"]: info for info in self.researcheManager.GetFrontData()}

        mainInfos = self.GetFrontData()
        return mainInfos, buildingInfos, resourceInfos, professionInfos, researchInfos

    def ApplyEffects(self, fromEntifyId : str, effects: list) :
        for effect in effects :
            effectType = effect.get("type", "")

            if effectType == "unlock" :
                target = effect.get("target", "")
                targetId = effect.get("id", "")
                if target == "resource" :
                    self.resourceManager.Unlock(targetId)
                elif target == "building" :
                    self.buildings.Unlock(targetId)
                elif target == "profession" :
                    self.professionManager.Unlock(targetId)
                elif target == "research" :
                    self.researcheManager.Unlock(targetId)
                continue

            if effectType == "produce" :
                resourceId = effect.get("resource", "")
                rate = effect.get("rate", 0)
                per = effect.get("per", "")
                if per == "click" :
                    self.resourceManager.AddAmount(resourceId, rate)
                elif per == "turn" :
                    self.resourceManager.ApplyCommonEffect(fromEntifyId, resourceId, effect)
                continue
            
            if effectType == "consume" :
                resourceId = effect.get("resource", "")
                rate = effect.get("rate", 0)
                per = effect.get("per", "")
                if per == "click" :
                    self.resourceManager.ClampAmount(resourceId, rate)
                elif per == "turn" :
                    self.resourceManager.ApplyCommonEffect(fromEntifyId, resourceId, effect)
                continue
            
            if effectType == "convert" :
                per = effect.get("per", "")
                if per == "click" :
                    inList = effect.get("inTargets", [])
                    outList = effect.get("outTarget", {})
                    self.resourceManager.ConvertAmount(inList, outList)
                elif per == "turn" :
                    self.resourceManager.ApplyConvertEffect(fromEntifyId, resourceId, effect)
                continue

            if effectType == "addJobSlot" :
                profession = effect.get("profession", "P_IDLE")
                self.professionManager.ApplyEffect(fromEntifyId, profession, effect)
                continue

        return
    
    def RevertEffects(self, fromEntifyId : str, effects: list) :
        for effect in self.professionManager.GetAllEffects(fromEntifyId) :
            effectType = effect.get("type", "")
            if effectType in ["produce", "consume"] :
                resourceId = effect.get("resource", "")
                if resourceId :
                    self.resourceManager.RevertCommonEffect(fromEntifyId, resourceId, effect)
                continue

            if effectType == "convert" :
                outTarget = effect.get("outTarget", {})
                outResourceId = outTarget.get("resourceId", "")
                if outResourceId :
                    self.resourceManager.RevertConvertEffect(fromEntifyId, outResourceId, effect)
                continue
        return

    def CheckPrereqs(self, prereqs: list) :
        for prereq in prereqs :
            pType = prereq.get("type", "")
            if pType == "hasBuilding" :
                if self.buildings.GetOwnedCount(prereq.get("id", "")) <= 0 :
                    return False
                continue
            if pType == "hasResearch" :
                if not self.researcheManager.IsFinished(prereq.get("id", "")) :
                    return False
                continue
        return True

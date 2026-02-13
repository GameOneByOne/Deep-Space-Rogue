import time
from collections import deque
from GameBuilding import BuildingManager
from GameResource import ResourceManager
from GameProfession import ProfessionManager
from GameResearch import ResearchManager
from GameEvent import EventManager
from GameEffect import EffectExecutor


BUILDING_DATA_PATH = "data/building.dat"
RESOURCE_DATA_PATH = "data/resource.dat"
PROFESSION_DATA_PATH = "data/profession.dat"
RESEARCH_DATA_PATH = "data/research.dat"
EVENT_DATA_PATH = "data/event.dat"

class GameEngine :
    def __init__(self) :
        # 初始化建筑数据
        self.buildingManager =  BuildingManager(BUILDING_DATA_PATH)

        # 初始化资源数据
        self.resourceManager = ResourceManager(RESOURCE_DATA_PATH)

        # 初始化人力数据
        self.professionManager = ProfessionManager(PROFESSION_DATA_PATH)

        # 初始化研究数据
        self.researcheManager = ResearchManager(RESEARCH_DATA_PATH)

        # 初始化事件数据
        self.eventManager = EventManager(EVENT_DATA_PATH)

        # 初始化效果执行器
        EffectExecutor.Init(self.buildingManager, self.resourceManager, self.professionManager, self.researcheManager)
        
        # 记录上次更新时间
        self.updateTime = int(time.time())

    def StartGame(self) :
        # 默认开局两个人力
        effect = { "type": "addLimit", "target": "profession", "id": "P_IDLE", "count": 2}
        self.ApplyEffects([EffectExecutor.FromDict(effect)])
        effect = { "type": "add", "target": "profession", "id": "P_IDLE", "count": 2}
        self.ApplyEffects([EffectExecutor.FromDict(effect)])
        return

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
        self.ApplyEffects(effects)
        return

    def Research(self, researchId: str) :
        # 研究未解锁或已完成，直接返回
        if not self.researcheManager.IsUnlocked(researchId) or self.researcheManager.IsFinished(researchId):
            return

        # 不够研究资源直接返回
        cost = self.researcheManager.GetResearchCost(researchId)
        if not self.resourceManager.IsEnough(cost) :
            return

        # 消耗研究资源并完成研究
        for item in cost :
            self.resourceManager.Clamp(item["id"], item["need"])

        effects = self.researcheManager.Finish(researchId)
        self.ApplyEffects(effects)
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
        self.ApplyEffects(revertEffects)
        self.ApplyEffects(newEffects)
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
        eventInfos = {info["id"]: info for info in self.researcheManager.GetFrontData()}
        mainInfos = self.GetFrontData()
        return mainInfos, buildingInfos, resourceInfos, professionInfos, researchInfos

    def ApplyEffects(self,  effects: list) :
        effectQue = deque(effects)
        while len(effectQue) > 0 :
            effectExec = effectQue.popleft()
            additionalEffect = EffectExecutor.Exec(effectExec)
            if additionalEffect is not None :
                effectQue.extend(additionalEffect)
        return

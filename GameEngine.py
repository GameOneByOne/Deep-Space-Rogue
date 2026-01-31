from GameBuilding import BuildingManager
from GameResource import ResourceManager
from GameProfession import ProfessionManager


BUILDING_DATA_PATH = "data/building.cfg"
RESOURCE_DATA_PATH = "data/resource.cfg"
PROFESSION_DATA_PATH = "data/profession.cfg"
RESEARCH_DATA_PATH = "data/research.cfg"


class GameEngine :
    def __init__(self) :
        # 初始化建筑数据
        self.buildings =  BuildingManager(BUILDING_DATA_PATH)
        # 初始化资源数据
        self.resourceManager = ResourceManager(RESOURCE_DATA_PATH)
        # 初始化人力职业数据
        self.professions = ProfessionManager(PROFESSION_DATA_PATH)

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
        self.ApplyImmediateEffects(effects)
        self.ApplyClickEffects(buildingId, effects)
        return True
    
    def Dispatch(self, professionId : str) :
        if not self.professions.IsUnlocked(professionId) :
            return False
        if professionId == "P_IDLE" :
            return False
        maxSlots = self.GetProfessionSlots(professionId)
        if self.professions.state[professionId].amount >= maxSlots :
            return False
        idle = self.professions.state.get("P_IDLE")
        if idle is None or idle.amount <= 0 :
            return False
        idle.amount -= 1
        self.professions.state[professionId].amount += 1
        return True

    def UnDispatch(self, professionId : str) :
        if not self.professions.IsUnlocked(professionId) :
            return False
        if professionId == "P_IDLE" :
            return False
        profState = self.professions.state[professionId]
        if profState.amount <= 0 :
            return False
        profState.amount -= 1
        self.professions.state["P_IDLE"].amount += 1
        return True
    
    def GetFrontData(self) :
        return

    def Tick(self) :
        for resState in self.resourceManager.state.values() :
            resState.producedRate = 0.0

        for buildingId, buildingState in self.buildings.state.items() :
            if not buildingState.unlocked or buildingState.ownedCount <= 0 :
                continue

            for effect in buildingState.buildingDef.effects :
                if not self.CheckCondition(effect.get("condition")) :
                    continue
                if effect.get("per") != "turn" :
                    continue
                self.ApplyTickEffect(buildingId, buildingState.ownedCount, effect)
        return


    def Show(self) :
        resourceInfos = {info["id"]: info for info in self.resourceManager.GetFrontData()}

        buildingInfos = {}
        for info in self.buildings.GetFrontData() :
            buildingId = info["id"]
            bDef = self.buildings.GetDef(buildingId)
            info["canBuild"] = self.resourceManager.IsEnough(bDef.cost)
            info["cost"] = self.ToCostMap(bDef.cost)
            info["canBuild"] = True
            buildingInfos[buildingId] = info

        professionInfos = {info["id"]: info for info in self.professions.GetFrontData()}

        mainInfos = self.GetFrontData()
        return mainInfos, buildingInfos, resourceInfos, professionInfos

    def ApplyImmediateEffects(self, effects: list) :
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
                    self.professions.Unlock(targetId)
            elif effectType == "addPeople" :
                count = effect.get("count", 0)
                profession = effect.get("profession", "P_IDLE")
                self.professions.AddPeople(count, profession)
        return

    def ApplyTickEffect(self, buildingId: str, ownedCount: int, effect: dict) :
        effectType = effect.get("type", "")
        if effectType == "produce" :
            resourceId = effect.get("resource", "")
            rate = effect.get("rate", 0) * ownedCount
            addBonus, mul = self.GetModifier(buildingId, "produce", resourceId, "")
            finalRate = (rate + addBonus) * mul
            if finalRate > 0 :
                self.resourceManager.AddAmount(resourceId, finalRate)
                self.resourceManager.state[resourceId].producedRate += finalRate
            return

        if effectType == "consume" :
            resourceId = effect.get("resource", "")
            rate = effect.get("rate", 0) * ownedCount
            available = min(rate, self.resourceManager.GetAmount(resourceId))
            if available > 0 :
                self.resourceManager.ClampAmount(resourceId, available)
                self.resourceManager.state[resourceId].producedRate -= available
            return

        if effectType == "convert" :
            inList = effect.get("in", [])
            outList = effect.get("out", [])
            if not inList or not outList :
                return
            ratio = 1.0
            for item in inList :
                need = item.get("amount", 0) * ownedCount
                if need <= 0 :
                    continue
                have = self.resourceManager.GetAmount(item.get("resource", ""))
                ratio = min(ratio, have / need if need > 0 else 0)
            if ratio <= 0 :
                return
            actualCount = ownedCount * ratio
            for item in inList :
                rid = item.get("resource", "")
                amount = item.get("amount", 0) * actualCount
                if amount > 0 :
                    self.resourceManager.ClampAmount(rid, amount)
                    self.resourceManager.state[rid].producedRate -= amount
            for item in outList :
                rid = item.get("resource", "")
                amount = item.get("amount", 0) * actualCount
                addBonus, mul = self.GetModifier(buildingId, "convert", "", rid)
                finalAmount = (amount + addBonus) * mul
                if finalAmount > 0 :
                    self.resourceManager.AddAmount(rid, finalAmount)
                    self.resourceManager.state[rid].producedRate += finalAmount
            return

        return

    def GetBuildingResourceFlow(self, effects: list, ownedCount: int, flowType: str) :
        flow = {}
        for effect in effects :
            if effect.get("per") != "turn" :
                continue
            effectType = effect.get("type", "")
            if flowType == "in" :
                if effectType == "consume" :
                    rid = effect.get("resource", "")
                    flow[rid] = flow.get(rid, 0) + effect.get("rate", 0) * ownedCount
                elif effectType == "convert" :
                    for item in effect.get("in", []) :
                        rid = item.get("resource", "")
                        flow[rid] = flow.get(rid, 0) + item.get("amount", 0) * ownedCount
            else :
                if effectType == "produce" :
                    rid = effect.get("resource", "")
                    flow[rid] = flow.get(rid, 0) + effect.get("rate", 0) * ownedCount
                elif effectType == "convert" :
                    for item in effect.get("out", []) :
                        rid = item.get("resource", "")
                        flow[rid] = flow.get(rid, 0) + item.get("amount", 0) * ownedCount
        return flow

    def ApplyClickEffects(self, buildingId: str, effects: list) :
        for effect in effects :
            if effect.get("per") != "click" :
                continue
            if not self.CheckCondition(effect.get("condition")) :
                continue
            self.ApplySingleEffect(buildingId, effect)
        return

    def ApplySingleEffect(self, buildingId: str, effect: dict) :
        effectType = effect.get("type", "")
        if effectType == "produce" :
            resourceId = effect.get("resource", "")
            rate = effect.get("rate", 0)
            addBonus, mul = self.GetModifier(buildingId, "produce", resourceId, "")
            finalRate = (rate + addBonus) * mul
            if finalRate > 0 :
                self.resourceManager.AddAmount(resourceId, finalRate)
            return

        if effectType == "consume" :
            resourceId = effect.get("resource", "")
            rate = effect.get("rate", 0)
            available = min(rate, self.resourceManager.GetAmount(resourceId))
            if available > 0 :
                self.resourceManager.ClampAmount(resourceId, available)
            return

        if effectType == "convert" :
            inList = effect.get("in", [])
            outList = effect.get("out", [])
            if not inList or not outList :
                return
            ratio = 1.0
            for item in inList :
                need = item.get("amount", 0)
                if need <= 0 :
                    continue
                have = self.resourceManager.GetAmount(item.get("resource", ""))
                ratio = min(ratio, have / need if need > 0 else 0)
            if ratio <= 0 :
                return
            for item in inList :
                rid = item.get("resource", "")
                amount = item.get("amount", 0) * ratio
                if amount > 0 :
                    self.resourceManager.ClampAmount(rid, amount)
            for item in outList :
                rid = item.get("resource", "")
                amount = item.get("amount", 0) * ratio
                addBonus, mul = self.GetModifier(buildingId, "convert", "", rid)
                finalAmount = (amount + addBonus) * mul
                if finalAmount > 0 :
                    self.resourceManager.AddAmount(rid, finalAmount)
            return

        return

    def ToCostMap(self, costList: list) :
        costMap = {}
        for item in costList :
            rid = item.get("id", "")
            costMap[rid] = costMap.get(rid, 0) + item.get("need", 0)
        return costMap

    def GetModifier(self, buildingId: str, effectType: str, resourceId: str, outResourceId: str) :
        addBonus = 0.0
        mul = 1.0

        for srcBuildingId, srcBuildingState in self.buildings.state.items() :
            if not srcBuildingState.unlocked or srcBuildingState.ownedCount <= 0 :
                continue
            for effect in srcBuildingState.buildingDef.effects :
                if effect.get("type") != "modifier" :
                    continue
                if not self.CheckCondition(effect.get("condition")) :
                    continue
                if not self.MatchScope(effect.get("scope", {}), buildingId, effectType, resourceId, outResourceId) :
                    continue
                addBonus, mul = self.AccumulateModifier(effect, srcBuildingState.ownedCount, addBonus, mul)

        for profState in self.professions.state.values() :
            if not profState.unlocked or profState.amount <= 0 :
                continue
            for effect in profState.profDef.effects :
                if effect.get("type") != "modifier" :
                    continue
                if not self.CheckCondition(effect.get("condition")) :
                    continue
                if not self.MatchScope(effect.get("scope", {}), buildingId, effectType, resourceId, outResourceId) :
                    continue
                addBonus, mul = self.AccumulateModifier(effect, profState.amount, addBonus, mul)

        return addBonus, mul

    def AccumulateModifier(self, effect: dict, count: int, addBonus: float, mul: float) :
        op = effect.get("op", "")
        value = effect.get("value", 0)
        if op == "add" :
            addBonus += value * count
        elif op == "mul" :
            mul *= value ** count
        else :
            addBonus += value * count
        return addBonus, mul

    def MatchScope(self, scope: dict, buildingId: str, effectType: str, resourceId: str, outResourceId: str) :
        if not scope :
            return True
        if scope.get("building", buildingId) != buildingId :
            return False
        if scope.get("effect", effectType) != effectType :
            return False
        if resourceId and scope.get("resource", resourceId) != resourceId :
            return False
        if outResourceId and scope.get("out", outResourceId) != outResourceId :
            return False
        return True

    def CheckCondition(self, cond: dict) :
        if not cond :
            return True
        condType = cond.get("type", "")
        if condType == "populationAtLeast" :
            return self.professions.population >= cond.get("value", 0)
        if condType == "jobFilled" :
            profId = cond.get("profession", "")
            profState = self.professions.state.get(profId)
            return profState is not None and profState.amount > 0
        if condType == "resourceAtLeast" :
            return self.resourceManager.GetAmount(cond.get("resource", "")) >= cond.get("value", 0)
        if condType == "hasBuilding" :
            return self.buildings.GetOwnedCount(cond.get("id", "")) > 0
        if condType == "hasResearch" :
            return False
        return True

    def GetProfessionSlots(self, professionId: str) :
        slots = 0
        for buildingState in self.buildings.state.values() :
            if not buildingState.unlocked or buildingState.ownedCount <= 0 :
                continue
            for effect in buildingState.buildingDef.effects :
                if effect.get("type") != "jobSlot" :
                    continue
                if effect.get("profession") != professionId :
                    continue
                slots += effect.get("slots", 0) * buildingState.ownedCount
        return slots

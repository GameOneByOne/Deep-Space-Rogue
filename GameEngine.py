# -*- coding: utf-8 -*-
from GameData import GameData, BUILDING_PREFIX, RESOURCE_PREFIX
from GameBuilding import BuildingItem
from GameResource import ResourceItem


class GameEngine :
    def __init__(self, data : GameData) :
        self.buildings = dict()
        self.resources = dict()
        for itemName, itemInfo in data.GetRawData().items() :
            # 初始化建筑数据
            if itemName.startswith(BUILDING_PREFIX) :
                self.buildings[itemName] = BuildingItem(itemInfo)
                continue

            # 初始化资源数据
            if itemName.startswith(RESOURCE_PREFIX) :
                self.resources[itemName] = ResourceItem(itemInfo)
                continue

    def IsResourceSufficient(self, needResoures : dict) :
        for id, num in needResoures.items() :
            if self.resources[id].count < num :
                return False
        return True
    
    def CostResources(self, costResources : dict ) :
        for id, num in costResources.items() :
            self.resources[id].count = self.resources[id].count - num
        return
    
    def ProduceResources(self, produceResources : dict) :
        for id, num in produceResources.items() :
            self.resources[id].count = min(self.resources[id].limit, self.resources[id].count + num)
        return
    
    def Build(self, buildingId : str) :
        if self.buildings.get(buildingId, None) == None:
            return

        costResource = self.buildings[buildingId].buildCostResources
        if not self.IsResourceSufficient(costResource) :
            return

        # 资源更新
        self.CostResources(costResource)
        if not self.buildings[buildingId].tickable :
            self.ProduceResources(self.buildings[buildingId].resourceOutput)

        # 判定解锁列表
        unlockBuildings, unlockResources = self.buildings[buildingId].Build()
        for buildingId in unlockBuildings :
            self.buildings[buildingId].unlock = True
        for resourceId in unlockResources :
            self.resources[resourceId].unlock = True

    def Tick(self) :
        for buildingItem in self.buildings.values() :
            if not buildingItem.unlock or not buildingItem.tickable :
                continue

            resourceInput, resourceOutput = buildingItem.Tick()
            if not self.IsResourceSufficient(resourceInput) :
                continue

            self.CostResources(resourceInput)
            self.ProduceResources(resourceOutput)

    def Show(self) :
        resourceInfos = dict()
        for resourceId, resourceInfo in self.resources.items() :
            if not resourceInfo.unlock :
                continue
            resourceInfos[resourceId] = dict()
            resourceInfos[resourceId]["id"] = resourceId
            resourceInfos[resourceId]["name"] = resourceInfo.info["name"]
            resourceInfos[resourceId]["describe"] = resourceInfo.info["describe"]
            resourceInfos[resourceId]["count"] = resourceInfo.count
            resourceInfos[resourceId]["limit"] = resourceInfo.limit
            resourceInfos[resourceId]["rate"] = 0

        buildingInfos = dict()
        for buildingId, buildingInfo in self.buildings.items() :
            if not buildingInfo.unlock :
                continue
            buildingInfos[buildingId] = dict()
            buildingInfos[buildingId]["id"] = buildingId
            buildingInfos[buildingId]["name"] = buildingInfo.info["name"]
            buildingInfos[buildingId]["describe"] = buildingInfo.info["describe"]
            buildingInfos[buildingId]["buildCostResources"] = buildingInfo.buildCostResources
            buildingInfos[buildingId]["resourceInput"] = buildingInfo.resourceInput
            buildingInfos[buildingId]["resourceOutput"] = buildingInfo.resourceOutput
            buildingInfos[buildingId]["count"] = buildingInfo.count

            # 统计上资源实际产出和消耗
            for resourceId, resourceRate in buildingInfo.actualResourceOutput.items() :
                if resourceId not in resourceInfos :
                    continue
                resourceInfos[resourceId]["rate"] += resourceRate
            for resourceId, resourceRate in buildingInfo.actualResourceInput.items() :
                if resourceId not in resourceInfos :
                    continue
                resourceInfos[resourceId]["rate"] -= resourceRate

        return buildingInfos, resourceInfos

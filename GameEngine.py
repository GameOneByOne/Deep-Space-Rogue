# -*- coding: utf-8 -*-
from GameData import GameData, BUILDING_PREFIX, RESOURCE_PREFIX
from GameBuilding import BuildingItem, BuildingType
from GameResource import ResourceItem


class GameEngine :
    def __init__(self, data : GameData) :
        self.buildings = dict()
        self.resources = dict()

        # 初始化建筑数据
        self.buildings = {itemName : BuildingItem(itemName, itemInfo) for itemName, itemInfo in data.GetBuildingData().items()}
        # 初始化资源数据
        self.resources = {itemName : ResourceItem(itemName, itemInfo) for itemName, itemInfo in data.GetResourceData().items()}

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
        if self.buildings[buildingId].type == BuildingType.REPEAT_CLICKABLE :
            self.ProduceResources(self.buildings[buildingId].actualResourceOutput)

        # 调用建筑的Build回调
        self.buildings[buildingId].Build(self.buildings, self.resources)

    def Tick(self) :
        for buildingItem in self.buildings.values() :
            if not buildingItem.unlock or buildingItem.type != BuildingType.TICKABLE :
                continue

            buildingItem.Tick(self.resources)

    def Show(self) :
        resourceInfos = dict()
        # 获取资源信息
        for resourceId, resourceInfo in self.resources.items() :
            if not resourceInfo.unlock :
                continue
            resourceInfos[resourceId] = resourceInfo.ToFrontDataFormat()

        # 获取建筑信息
        buildingInfos = dict()
        for buildingId, buildingInfo in self.buildings.items() :
            if not buildingInfo.unlock :
                continue
            buildingInfos[buildingId] = buildingInfo.ToFrontDataFormat()

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

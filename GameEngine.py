# -*- coding: utf-8 -*-
from GameData import GameData, BUILDING_PREFIX, RESOURCE_PREFIX
from GameBuilding import BuildingItem, BuildingType
from GameResource import ResourceItem
from GameProfession import ProfessionItem


class GameEngine :
    def __init__(self, data : GameData) :
        # 初始化建筑数据
        self.buildings = {itemName : BuildingItem(itemName, itemInfo) for itemName, itemInfo in data.GetBuildingData().items()}
        # 初始化资源数据
        self.resources = {itemName : ResourceItem(itemName, itemInfo) for itemName, itemInfo in data.GetResourceData().items()}
        # 初始化人力数据
        self.professions = {itemName : ProfessionItem(itemName, itemInfo) for itemName, itemInfo in data.GetProfessionData().items()}
    
    def Build(self, buildingId : str) :
        self.buildings[buildingId].Build(self.buildings, self.resources, self.professions)
        return
    
    def Dispatch(self, professionId : str) :
        self.professions[professionId].Dispatch(self.professions)
        return

    def UnDispatch(self, professionId : str) :
        self.professions[professionId].UnDispatch(self.professions)
        return
    
    def ToFrontDataFormat(self) :
        data = dict()
        return data

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
        
        # 获取人力信息
        professionInfos = dict()
        for professionId, professionInfo in self.professions.items() :
            if not professionInfo.unlock :
                continue
            professionInfos[professionId] = professionInfo.ToFrontDataFormat()
        
        # 获取游戏信息
        mainInfos = self.ToFrontDataFormat()
        return mainInfos, buildingInfos, resourceInfos, professionInfos

from enum import Enum


class BuildingType(Enum) :
    ONCE_CLICKABLE = 0
    REPEAT_CLICKABLE = 1
    TICKABLE = 2
    UNKNOWN = 3


class BuildingItem :
    def __init__(self, id : str, info : dict) :
        # 预置的成员变量，来自于数据文件
        self.info = info
        self.id = id
        self.name = self.info.get("name", "未知物品 - {}".format(self.id))
        self.description = self.info.get("description", "无描述")
        self.type = BuildingType(self.info.get("type", 3))
        self.unlock = self.info.get("defaultLockState", False)

        self.resourceInput = dict()
        resourceInputList = self.info.get("resourceInput", list())
        for resource in resourceInputList :
            self.resourceInput[resource["id"]] = resource["rate"]

        self.resourceOutput = dict()
        resourceOutputList = self.info.get("resourceOutput", list())
        for resource in resourceOutputList :
            self.resourceOutput[resource["id"]] = resource["rate"]
        
        self.storageBuff = dict()
        storageBuffList = self.info.get("storageBuff", list())
        for resource in storageBuffList :
            self.storageBuff[resource["id"]] = resource["buff"]
        
        self.buildCostResources = dict()
        buildCostResourcesList = self.info.get("buildCostResources", list())
        for resource in buildCostResourcesList :
            self.buildCostResources[resource["id"]] = resource["cost"]
        
        self.unlockBuildings = self.info.get("willLockBuilding", list())
        self.unlockResources = self.info.get("willLockResource", list())

        # 自定义的成员变量
        self.count = 0 if self.type == BuildingType.TICKABLE else 1
        self.actualResourceInput = {resourceId : rate * self.count for resourceId, rate in self.resourceInput.items()}
        self.actualResourceOutput = {resourceId : rate * self.count for resourceId, rate in self.resourceOutput.items()}

    def Build(self, mainBuildings : dict , mainResources : dict) :
        # 资源更新
        if self.type == BuildingType.TICKABLE :
            self.count += 1
            self.actualResourceInput = {resourceId : rate * self.count for resourceId, rate in self.resourceInput.items()}
            self.actualResourceOutput = {resourceId : rate * self.count for resourceId, rate in self.resourceOutput.items()}
    
        # 解锁建筑和资源
        for buildingId in self.unlockBuildings :
            mainBuildings[buildingId].unlock = True
        for resourceId in self.unlockResources :
            mainResources[resourceId].unlock = True

        # 更新资源输入输出
        if self.IsResourceSufficientForInput(mainResources) :
            return
        for resourceId, count in self.actualResourceInput.items() :
            mainResources[resourceId].count -= count
        for resourceId, count in self.actualResourceOutput.items() :
            mainResources[resourceId].count += count
        return

    def Tick(self, mainResources : dict) :
        if self.IsResourceSufficientForInput(mainResources) :
            return
        for resourceId, count in self.actualResourceInput.items() :
            mainResources[resourceId].count -= count
        for resourceId, count in self.actualResourceOutput.items() :
            mainResources[resourceId].count += count

        return
    
    def ToFrontDataFormat(self) :
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["description"] = self.description
        data["type"] = self.type.value
        data["count"] = self.count
        data["buildCostResources"] = self.buildCostResources
        data["resourceInput"] = self.resourceInput
        data["resourceOutput"] = self.resourceOutput
        return data
    
    def IsResourceSufficientForInput(self, resources : dict) :
        for resourceId, count in self.actualResourceInput.items() :
            if not (resources.get(resourceId, 0) >= count) :
                return False
        return True

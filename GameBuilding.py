

class BuildingItem :
    def __init__(self, info : dict) :
        self.info = info
        self.count = 0
        self.tickable = self.info.get("tickable", True)
        self.unlock = self.info.get("defaultLockState", False)
        self.buildCostResources = dict()
        self.resourceInput = dict()
        self.resourceOutput = dict()

        resourceInputList = self.info.get("resourceInput", list())
        for resource in resourceInputList :
            self.resourceInput[resource["id"]] = resource["rate"]

        resourceOutputList = self.info.get("resourceOutput", list())
        for resource in resourceOutputList :
            self.resourceOutput[resource["id"]] = resource["rate"]

        buildCostResourcesList = self.info.get("buildCostResources", list())
        for resource in buildCostResourcesList :
            self.buildCostResources[resource["id"]] = resource["cost"]

        self.actualResourceInput = {resourceId : rate * self.count for resourceId, rate in self.resourceInput.items()}
        self.actualResourceOutput = {resourceId : rate * self.count for resourceId, rate in self.resourceOutput.items()}

    def Build(self) :
        if self.tickable :
            self.count += 1
            self.actualResourceInput = {resourceId : rate * self.count for resourceId, rate in self.resourceInput.items()}
            self.actualResourceOutput = {resourceId : rate * self.count for resourceId, rate in self.resourceOutput.items()}

        return self.info.get("willLockBuilding", list()), self.info.get("willLockResource", list())

    def Tick(self) :
        return self.actualResourceInput, self.actualResourceOutput

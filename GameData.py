import json


BUILDING_PREFIX = "B"
BUILDING_DATA_PATH = "data/building.cfg"

RESOURCE_PREFIX = "R"
RESOURCE_DATA_PATH = "data/resource.cfg"

PEOPLE_PREFIX = "P"
PEOPLE_DATA_PATH = "data/profession.cfg"

RESEARCH_PREFIX = "S"
RESEARCH_DATA_PATH = "data/research.cfg"

class GameData :
    def __init__(self) :
        self.buildingData = dict()
        self.resourceData = dict()
        self.professionData = dict()
        self.researchData = dict()

        with open(BUILDING_DATA_PATH, "r", encoding="utf-8") as f :
            self.buildingData = json.loads(f.read())
        with open(RESOURCE_DATA_PATH, "r", encoding="utf-8") as f :
            self.resourceData = json.loads(f.read())
        with open(PEOPLE_DATA_PATH, "r", encoding="utf-8") as f :
            self.professionData = json.loads(f.read())
        with open(RESEARCH_DATA_PATH, "r", encoding="utf-8") as f :
            self.researchData = json.loads(f.read())

    def GetItemName(self, ItemId) :
        if ItemId.startswith(BUILDING_PREFIX) :
            return self.buildingData.get(ItemId, {"name":"Unknown"})["name"]
        elif ItemId.startswith(RESOURCE_PREFIX) :
            return self.resourceData.get(ItemId, {"name":"Unknown"})["name"]
        elif ItemId.startswith(PEOPLE_PREFIX) :
            return self.professionData.get(ItemId, {"name":"Unknown"})["name"]
        elif ItemId.startswith(RESEARCH_PREFIX) :
            return self.researchData.get(ItemId, {"name":"Unknown"})["name"]

        return 

    def GetBuildingData(self) :
        return self.buildingData
    
    def GetResourceData(self) :
        return self.resourceData

    def GetProfessionData(self) :
        return self.professionData

    def GetResearchData(self) :
        return self.researchData

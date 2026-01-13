import json


BUILDING_PREFIX = "B"
RESOURCE_PREFIX = "R"

class GameData :
    def __init__(self, dataPath : str) :
        with open(dataPath, "r", encoding="utf-8") as f :
            self.data = json.loads(f.read())

    def GetItemName(self, ItemId) :
        return self.data.get(ItemId, {"name":"Unknown"})["name"]

    def GetRawData(self) :
        return self.data

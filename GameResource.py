
class ResourceItem :
    def __init__(self, id : str, info : dict) :
        self.id = id
        self.info = info
        self.name = self.info.get("name", "未知物品 - {}".format(self.id))
        self.description = self.info.get("description", "未知描述")
        self.unlock = self.info.get("defaultLockState", False)
        self.count = 0
        self.limit = 100

    def ToFrontDataFormat(self) :
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["description"] = self.description
        data["count"] = self.count
        data["limit"] = self.limit
        data["rate"] = 0
        return data

IDLE_PROFESSION_ID = "P00000"


class ProfessionItem :
    def __init__(self, id : str, info : dict) :
        self.id = id
        self.info = info
        self.name = self.info.get("name", "未知职业 - {}".format(self.id))
        self.description = self.info.get("description", "未知描述")
        self.canEdit = self.info.get("canEdit", True)
        self.unlock = self.info.get("defaultUnlockState", False)
        self.count = 0

    def Dispatch(self, mainProfessions : str) :
        if mainProfessions[IDLE_PROFESSION_ID].count == 0 :
            return

        mainProfessions[IDLE_PROFESSION_ID].count -= 1
        self.count += 1
        return

    def UnDispatch(self, mainProfessions : str) :
        if self.count == 0 :
            return
    
        self.count -= 1
        mainProfessions[IDLE_PROFESSION_ID].count += 1
        return

    def ToFrontDataFormat(self) :
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["description"] = self.description
        data["count"] = self.count
        data["canEdit"] = self.canEdit
        return data
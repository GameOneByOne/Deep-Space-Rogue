
class ResourceItem :
    def __init__(self, info : dict) :
        self.info = info
        self.unlock = self.info.get("defaultLockState", False)
        self.count = 0
        self.limit = 100
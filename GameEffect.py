from __future__ import annotations

class Effect :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        self.raw = raw
        self.fromId = fromEntityId
        self.belongTo = belongTo
        self.onlyOnce = True

    def Apply(self) :
        return
    
    def Revert(self) :
        return

    def IsOnlyOnce(self) :
        return self.onlyOnce


class UnlockEffect(Effect) :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        super().__init__(fromEntityId, raw, belongTo)
        self.toId = raw.get("id", "")
    
    def Apply(self) :
        self.belongTo.Unlock(self.toId)
        return
    
    def Revert(self) :
        return


class AddEffect(Effect) :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        super().__init__(fromEntityId, raw, belongTo)
        self.toId = raw.get("id", "")
        self.count = raw.get("count", 0)
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True

    def Apply(self) :
        self.belongTo.ApplyEffect(self.fromId, self.toId, self)
        return
    
    def Revert(self) :
        self.belongTo.RevertEffect(self.fromId, self.toId, self)
        return
                

class ClampEffect(Effect) :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        super().__init__(fromEntityId, raw, belongTo)
        self.count = raw.get("count", 0)
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True

    def Apply(self) :
        self.belongTo.ApplyEffect(self.fromId, self.toId, self)
        return
    
    def Revert(self) :
        self.belongTo.RevertEffect(self.fromId, self.toId, self)
        return


class ConvertEffect(Effect) :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        super().__init__(fromEntityId, raw, belongTo)
        self.toId = ""
        self.inTargets = raw.get("inTargets", [])
        self.outTarget = raw.get("outTarget", {})
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True

    def Apply(self) :
        self.belongTo.ApplyEffect(self.fromId, self.toId, self)
        return

    def Revert(self) :
        self.belongTo.RevertEffect(self.fromId, self.toId, self)
        return


class ModifierEffect(Effect) :
    def __init__(self, fromEntityId:str, raw: dict, belongTo) :
        super().__init__(fromEntityId, raw, belongTo)
        self.scope = raw.get("scope", {})
        self.op = raw.get("op", "")
        self.value = raw.get("value", 0)
        self.condition = raw.get("condition", {})


class EffectExecutor :
    def __init__(self, buildingManager, resourceManager, professionManager, researchManager) :
        self.buildingManager = buildingManager
        self.resourceManager = resourceManager
        self.professionManager = professionManager
        self.researchManager = researchManager

    def FromDict(self, fromEntityId: str, effect: list) :
        effectType = effect.get("type", "")
        target = effect.get("target", "")

        if effectType == "unlock" :
            if target == "resource" :
                return UnlockEffect(fromEntityId, effect, self.resourceManager)
            elif target == "building" :
                return UnlockEffect(fromEntityId, effect, self.buildingManager)
            elif target == "profession" :
                return UnlockEffect(fromEntityId, effect, self.professionManager)
            elif target == "research" :
                return UnlockEffect(fromEntityId, effect, self.researchManager)
            return Effect(fromEntityId, effect, None)

        if effectType == "add" :
            if target == "resource" :
                return AddEffect(fromEntityId, effect, self.resourceManager)
            elif target == "profession" :
                return AddEffect(fromEntityId, effect, self.professionManager)
            return Effect(fromEntityId, effect, None)

        if effectType == "clamp" :
            if target == "resource" :
                return ClampEffect(fromEntityId, effect, self.resourceManager)
            elif target == "profession" :
                return ClampEffect(fromEntityId, effect, self.professionManager)
            return Effect(fromEntityId, effect, None)

        if effectType == "convert" :
            if target == "resource" :
                return ClampEffect(fromEntityId, effect, self.resourceManager)
            return Effect(fromEntityId, effect, None)

        return Effect(fromEntityId, effect, None)

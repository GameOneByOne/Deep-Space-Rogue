from __future__ import annotations

class Effect :
    def __init__(self, raw: dict = dict()) :
        self.target = raw.get("target", "")
        self.toId = raw.get("id", "")
        self.onlyOnce = True
    
    def GetOppositeEffect(self) :
        return Effect()


class UnlockEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)


class AddEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.count = raw.get("count", 0)
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True

    def GetOppositeEffect(self) :
        effect = ClampEffect()
        effect.target = self.target
        effect.toId = self.toId
        effect.count = self.count
        effect.per = self.per
        effect.condition = self.condition
        effect.onlyOnce = self.onlyOnce
        return effect
                

class ClampEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.count = raw.get("count", 0)
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True

    def GetOppositeEffect(self) :
        effect = AddEffect()
        effect.target = self.target
        effect.toId = self.toId
        effect.count = self.count
        effect.per = self.per
        effect.condition = self.condition
        effect.onlyOnce = self.onlyOnce
        return effect


class ConvertEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.inTargets = raw.get("inTargets", [])
        self.outTarget = raw.get("outTarget", {})
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True


class AddLimitEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.count = raw.get("count", 0)


class ModifierEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.scope = raw.get("scope", {})
        self.op = raw.get("op", "")
        self.value = raw.get("value", 0)
        self.condition = raw.get("condition", {})


class EffectExecutor :
    buildingManager = None
    resourceManager = None
    professionManager = None
    researchManager = None

    @staticmethod
    def Init(buildingManager, resourceManager, professionManager, researchManager) :
        EffectExecutor.buildingManager = buildingManager
        EffectExecutor.resourceManager = resourceManager
        EffectExecutor.professionManager = professionManager
        EffectExecutor.researchManager = researchManager

    @staticmethod
    def FromDict(effect: dict) :
        effectType = effect.get("type", "")

        if effectType == "unlock" :
            return UnlockEffect(effect)

        if effectType == "add" :
            return AddEffect(effect)

        if effectType == "clamp" :
            return ClampEffect(effect)

        if effectType == "convert" :
            return ConvertEffect(effect)

        if effectType == "addLimit" :
            return AddLimitEffect(effect)   

        return Effect(effect, None)

    @staticmethod
    def Exec(effect: Effect) :
        if effect.target == "resource" :
            return EffectExecutor.resourceManager.ApplyEffect(effect)

        if effect.target == "building" :
            return EffectExecutor.buildingManager.ApplyEffect(effect)

        if effect.target == "profession" :
            return EffectExecutor.professionManager.ApplyEffect(effect)

        if effect.target == "research" :
            return EffectExecutor.researchManager.ApplyEffect(effect)
        
        return

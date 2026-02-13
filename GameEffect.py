from __future__ import annotations

TARGET_NAME_CONVERT = {
    "resource" :"资源",
    "building" :"建筑",
    "profession" :"职业",
    "research" :"研究"
}

PER_NAME_CONVERT= {
    "turn" : "每秒",
    "click": "每次点击"
}

class Effect :
    def __init__(self, raw: dict = dict()) :
        self.target = raw.get("target", "")
        self.toId = raw.get("id", "")
        self.onlyOnce = True
    
    def GetOppositeEffect(self) :
        return Effect()
    
    def __str__(self) :
        return "无效果"


class UnlockEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)

    def __str__(self) :
        return "解锁" + TARGET_NAME_CONVERT[self.target] + ": " + EffectExecutor.GetEntityName(self.toId)


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
    
    def __str__(self) :
        return PER_NAME_CONVERT[self.per] + "增加" + EffectExecutor.GetEntityName(self.toId) + TARGET_NAME_CONVERT[self.target] + \
            ": " + str(self.count)
                

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

    def __str__(self) :
        return PER_NAME_CONVERT[self.per] + "减少" + EffectExecutor.GetEntityName(self.toId) + TARGET_NAME_CONVERT[self.target] + \
            ": " + str(self.count)

class ConvertEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.inTargets = raw.get("inTargets", [])
        self.outTarget = raw.get("outTarget", {})
        self.per = raw.get("per", "")
        self.condition = raw.get("condition", {})
        self.onlyOnce = False if self.per == "turn" else True
    
    def __str__(self) :
        return "转换作用"


class AddLimitEffect(Effect) :
    def __init__(self, raw: dict = dict()) :
        super().__init__(raw)
        self.count = raw.get("count", 0)

    def __str__(self) :
        return "增加" + EffectExecutor.GetEntityName(self.toId) + TARGET_NAME_CONVERT[self.target] + "上限: " + str(self.count)


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
    entityIdToName = dict()

    @staticmethod
    def Init(buildingManager, resourceManager, professionManager, researchManager) :
        EffectExecutor.buildingManager = buildingManager
        EffectExecutor.resourceManager = resourceManager
        EffectExecutor.professionManager = professionManager
        EffectExecutor.researchManager = researchManager

        # 保存ID和名字的映射关系
        for bState in buildingManager.state.values() :
            EffectExecutor.entityIdToName[bState.buildingDef.id] = bState.buildingDef.name
        for rState in resourceManager.state.values() :
            EffectExecutor.entityIdToName[rState.resDef.id] = rState.resDef.name
        for pState in professionManager.state.values() :
            EffectExecutor.entityIdToName[pState.profDef.id] = pState.profDef.name
        for rState in researchManager.state.values() :
            EffectExecutor.entityIdToName[rState.researchDef.id] = rState.researchDef.name

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

    @staticmethod
    def GetEntityName(id: str) :
        if id not in EffectExecutor.entityIdToName:
            return ""
        return EffectExecutor.entityIdToName[id]

    @staticmethod
    def GetCostDesc(cost: dict) :
        return "{}: {}".format(EffectExecutor.GetEntityName(cost["id"]), cost["need"])

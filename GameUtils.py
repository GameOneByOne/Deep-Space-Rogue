

def JoinDesc(mainText: str, condText: str) -> str:
    if not condText :
        return mainText
    return f"当{condText}时，{mainText}"

def FormatResList(resList: list) -> str:
    parts = []
    for item in resList :
        resource = item.get("resource", "")
        amount = item.get("need", 0)
        parts.append(f"{amount}单位{resource}")
    return " + ".join(parts)

def FormatScope(scope: dict) -> str:
    if not scope :
        return "对目标"
    parts = []
    if "building" in scope :
        parts.append(f"{scope.get('building')}")
    if "effect" in scope :
        parts.append(f"{scope.get('effect')}")
    if "resource" in scope :
        parts.append(f"{scope.get('resource')}")
    if "inTargets" in scope :
        parts.append(f"in={scope.get('in')}")
    if "outTarget" in scope :
        parts.append(f"out={scope.get('out')}")
    return " ".join(parts)

def GetOpText(op: str, value) -> str:
    if op == "add" :
        return f"+{value}"
    if op == "mul" :
        return f"x{value}"
    if not op :
        return f"{value}"
    return f"{op} {value}"

def GetConditionDesc(cond: dict) -> str:
    if not cond :
        return ""
    condType = cond.get("type", "")
    if condType == "populationAtLeast" :
        return f"人口不少于 {cond.get('value', 0)}"
    if condType == "jobFilled" :
        return f"岗位已配置 {cond.get('profession', '')}"
    if condType == "resourceAtLeast" :
        return f"{cond.get('resource', '')} 不少于 {cond.get('value', 0)}"
    if condType == "hasBuilding" :
        return f"拥有建筑 {cond.get('id', '')}"
    if condType == "hasResearch" :
        return f"拥有研究 {cond.get('id', '')}"
    return f"{condType} {cond}"


TARGET_NAME_CONVERT = {
    "resource" :"资源",
    "building" :"建筑",
    "profession" :"职业",
    "research" :"研究"
}

PER_NAME_CONVERT= {
    "turn" : "每回合",
    "click": "每次点击"
}

class EffectUtils :
    entityIdToName = dict()

    @staticmethod
    def AddEntityToNameMap(entityId : str, name : str) :
        EffectUtils.entityIdToName[entityId] = name
        return

    @staticmethod
    def GetEntityName(entityId: str) :
        return EffectUtils.entityIdToName.get(entityId, entityId)

    @staticmethod
    def GetEffectDesc(effect : dict) :
        effectType = effect.get("type", "")
        cond = GetConditionDesc(effect.get("condition"))

        if effectType == "unlock" :
            target = TARGET_NAME_CONVERT[effect.get("target", "")]
            targetId = effect.get("id", "")
            return JoinDesc(f"解锁{target}: {EffectUtils.GetEntityName(targetId)}", cond)

        if effectType == "produce" :
            resource = effect.get("resource", "")
            rate = effect.get("rate", 0)
            perText = PER_NAME_CONVERT[effect.get("per", "")]
            return JoinDesc(f"{perText}产出{rate}单位{EffectUtils.GetEntityName(resource)}", cond)

        if effectType == "consume" :
            resource = effect.get("resource", "")
            rate = effect.get("rate", 0)
            perText = PER_NAME_CONVERT[effect.get("per", "")]
            return JoinDesc(f"{perText}消耗{rate}单位{EffectUtils.GetEntityName(resource)}", cond)

        if effectType == "convert" :
            inList = effect.get("inTargets", [])
            outList = effect.get("outTarget", {})
            perText = PER_NAME_CONVERT[effect.get("per", "")]
            inText = FormatResList(inList)
            outText = FormatResList(outList)
            return JoinDesc(f"{perText}将 {inText} 转化为 {outText}", cond)

        if effectType == "addJobSlot" :
            profession = effect.get("profession", "")
            slots = effect.get("slots", 0)
            return JoinDesc(f"提供{EffectUtils.GetEntityName(profession)}岗位{slots}个", cond)

        if effectType == "modifier" :
            scope = effect.get("scope", {})
            op = effect.get("op", "")
            value = effect.get("value", 0)
            scopeText = FormatScope(scope)
            opText = GetOpText(op, value)
            return JoinDesc(f"{scopeText} {opText}", cond)

        if effectType == "addPeople" :
            count = effect.get("count", 0)
            profession = effect.get("profession", "")
            return JoinDesc(f"增加人口 {count}（{EffectUtils.GetEntityName(profession)}）", cond)

        if not effectType :
            return "未知效果"
        return f"效果: {effectType}"

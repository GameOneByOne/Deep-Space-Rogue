

def JoinDesc(mainText: str, condText: str) -> str:
    if not condText :
        return mainText
    return f"当{condText}时，{mainText}"


def GetEntityDisplayName(entityId: str) -> str:
    return Utils.GetEntityName(entityId)

def FormatResList(resList: list) -> str:
    if isinstance(resList, dict) :
        resList = [resList]
    parts = []
    for item in resList :
        resource = item.get("resource", item.get("resourceId", ""))
        amount = item.get("need", item.get("amount", 0))
        parts.append(f"{amount}单位{Utils.GetEntityName(resource)}")
    return " + ".join(parts)

def FormatScope(scope: dict) -> str:
    if not scope :
        return "对目标"
    parts = []
    if "building" in scope :
        parts.append(f"{GetEntityDisplayName(scope.get('building'))}")
    if "effect" in scope :
        parts.append(f"{scope.get('effect')}")
    if "resource" in scope :
        parts.append(f"{GetEntityDisplayName(scope.get('resource'))}")
    if "inTargets" in scope :
        parts.append(f"in={scope.get('inTargets')}")
    if "outTarget" in scope :
        parts.append(f"out={Utils.GetEntityName(scope.get('outTarget'))}")
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
        return f"岗位已配置 {Utils.GetEntityName(cond.get('profession', ''))}"
    if condType == "resourceAtLeast" :
        return f"{Utils.GetEntityName(cond.get('resource', ''))} 不少于 {cond.get('value', 0)}"
    if condType == "hasBuilding" :
        return f"拥有建筑 {Utils.GetEntityName(cond.get('id', ''))}"
    if condType == "hasResearch" :
        return f"拥有研究 {Utils.GetEntityName(cond.get('id', ''))}"
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

class Utils :
    entityIdToName = dict()

    @staticmethod
    def AddEntityToNameMap(entityId : str, name : str) :
        Utils.entityIdToName[entityId] = name
        return

    @staticmethod
    def GetEntityName(entityId: str) :
        return Utils.entityIdToName.get(entityId, entityId)

    @staticmethod
    def GetCostDesc(cost: dict) :
        return "{}: {}".format(Utils.GetEntityName(cost["id"]), cost["need"])

    @staticmethod
    def GetEffectDesc(effect : dict) :
        effectType = effect.get("type", "")
        cond = GetConditionDesc(effect.get("condition"))

        if effectType == "unlock" :
            target = TARGET_NAME_CONVERT[effect.get("target", "")]
            targetId = effect.get("id", "")
            return JoinDesc(f"解锁{target}: {Utils.GetEntityName(targetId)}", cond)

        if effectType == "add" :
            target = effect.get("target", "")
            targetId = effect.get("id", "")
            count = effect.get("count", 0)
            perText = PER_NAME_CONVERT.get(effect.get("per", ""), "")
            if target == "resource" :
                return JoinDesc(f"{perText}增加{count}单位{Utils.GetEntityName(targetId)}", cond)
            if target == "profession" :
                if targetId == "P_IDLE" :
                    return JoinDesc(f"增加人口 {count}", cond)
                return JoinDesc(f"提供{Utils.GetEntityName(targetId)}岗位{count}个", cond)

        if effectType == "clamp" :
            target = effect.get("target", "")
            targetId = effect.get("id", "")
            count = effect.get("count", 0)
            perText = PER_NAME_CONVERT.get(effect.get("per", ""), "")
            if target == "resource" :
                return JoinDesc(f"{perText}消耗{count}单位{Utils.GetEntityName(targetId)}", cond)
            if target == "profession" :
                if targetId == "P_IDLE" :
                    return JoinDesc(f"减少人口 {count}", cond)
                return JoinDesc(f"减少{Utils.GetEntityName(targetId)}岗位{count}个", cond)

        if effectType == "convert" :
            inList = effect.get("inTargets", [])
            outList = effect.get("outTarget", {})
            perText = PER_NAME_CONVERT[effect.get("per", "")]
            inText = FormatResList(inList)
            outText = FormatResList(outList)
            return JoinDesc(f"{perText}将 {inText} 转化为 {outText}", cond)

        if effectType == "modifier" :
            scope = effect.get("scope", {})
            op = effect.get("op", "")
            value = effect.get("value", 0)
            scopeText = FormatScope(scope)
            opText = GetOpText(op, value)
            return JoinDesc(f"{scopeText} {opText}", cond)

        if not effectType :
            return "未知效果"
        return f"效果: {effectType}"

import tkinter as tk
from functools import partial
from Tooltip import Tooltip
from GameUtils import GetEntityDisplayName


class ResourceItemUI :
    def __init__(self, root, ) :
        self.resourceCountAndRateVar = tk.StringVar()
        self.resourceLabelWidget = tk.Label(root, textvariable=self.resourceCountAndRateVar, height=1, width=25,  bg="#f0f0f0")
        self.resourceLabelWidget.pack(side=tk.TOP, padx=5, anchor="nw")

    def Update(self, content) :
        resourceTitle = content["name"].ljust(6 - len(content["name"]))
        countText = FormatNumber(content["count"])
        limitText = FormatNumber(content["limit"])
        resourceCountAndLimit = (": {}/{}".format(countText, limitText)).ljust(10)
        resourceRate = ""
        if (content["rate"] >= 0) :
            resourceRate = "+{:.2f}".format(content["rate"]).rjust(7)
        else :
            resourceRate = "-{:.2f}".format(content["rate"]).rjust(7)

        self.resourceCountAndRateVar.set(resourceTitle + resourceCountAndLimit + resourceRate)
        return


def FormatNumber(value) -> str:
    try :
        text = "{:.3f}".format(float(value))
    except (TypeError, ValueError) :
        return str(value)
    text = text.rstrip("0").rstrip(".")
    return text if text else "0"


class BuildingItemUI :
    def __init__(self, id, root, gameEngine) :
        self.gameEngine = gameEngine
        self.buttonTextVar = tk.StringVar()
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonWidget = tk.Button(root, textvariable=self.buttonTextVar, height=1, width=10, bg="#f0f0f0", command=partial(self.Build, id))
        self.buttonWidget.pack(side=tk.LEFT, padx=5, anchor="nw")
        Tooltip(self.buttonWidget, self.buttonTooltipTextVar)

    def Update(self, content : dict) :
        # 更新按钮文本
        if content["count"] != 0 :
            self.buttonTextVar.set(content["name"] + "({})".format(content["count"]))
        else :
            self.buttonTextVar.set(content["name"])

        # 更新按钮状态
        self.buttonWidget.config(state=tk.ACTIVE if content["canBuild"] else tk.DISABLED)

        # 更新按钮提示文本
        tooltipText = "-----------描述-----------\n"
        tooltipText += content["desc"] + "\n"
        cost = content.get("cost", [])
        if len(cost) > 0 :
            tooltipText += "-----------建造消耗-----------\n"
            for item in cost :
                tooltipText += "{}: {}\n".format(GetEntityDisplayName(item.get("id", "")), item.get("need", 0))
        tooltipText += "-----------效果-----------\n"
        for effect in content["effects"] :
            tooltipText += effect
            tooltipText += "\n"
        self.buttonTooltipTextVar.set(tooltipText)

        return

    def Build(self, buildingId : str) :
        self.gameEngine.Build(buildingId)
        return
    

class ProfessionButtonUI :
    def __init__(self, id, root, gameEngine, canEdit) :
        self.gameEngine = gameEngine
        self.buttonTextVar = tk.StringVar()
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonFrameWidget= tk.Frame(root, relief="solid", borderwidth=1, width=50, height=30, bg="white")
        self.professionLabelWidget = tk.Label(self.buttonFrameWidget, height=1, width=10, bg="#f0f0f0")
        self.professionLabelWidget.pack(side=tk.LEFT, padx=5)
        
        self.professionAddButtonWidget = tk.Button(self.buttonFrameWidget, text="+", height=1, width=1, bg="#f0f0f0", command=partial(self.Dispatch, id))
        self.professionSubButtonWidget = tk.Button(self.buttonFrameWidget, text="-", height=1, width=1, bg="#f0f0f0", command=partial(self.UnDispatch, id))
        if canEdit :           
            self.professionAddButtonWidget.pack(side=tk.RIGHT)
            self.professionSubButtonWidget.pack(side=tk.RIGHT)
        self.buttonFrameWidget.pack(side=tk.TOP, padx=5, anchor="nw")
        Tooltip(self.buttonFrameWidget, self.buttonTooltipTextVar)

    def Update(self, content : dict) :
        if content["limit"] < 0 :
            self.professionLabelWidget.config(text="{}: {}".format(content["name"], content["count"]))
        else :
            self.professionLabelWidget.config(text="{}: {}/{}".format(content["name"], content["count"], content["limit"]))

        tooltipText = "-----------描述-----------\n"
        tooltipText += content["desc"] + "\n"
        if len(content["effects"]) > 0 :
            tooltipText += "-----------效果-----------\n"
            for effect in content["effects"] :
                tooltipText += effect + "\n"
        self.buttonTooltipTextVar.set(tooltipText)

    def Dispatch(self, professionId : str) :
        self.gameEngine.Dispatch(professionId)
        return

    def UnDispatch(self, professionId : str) :
        self.gameEngine.UnDispatch(professionId)
        return


class ResearchItemUI :
    def __init__(self, id, root, gameEngine) :
        self.gameEngine = gameEngine
        self.buttonTextVar = tk.StringVar()
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonWidget = tk.Button(root, textvariable=self.buttonTextVar, height=1, width=12, bg="#f0f0f0", command=partial(self.Research, id))
        self.buttonWidget.pack(side=tk.LEFT, padx=5, anchor="nw")
        Tooltip(self.buttonWidget, self.buttonTooltipTextVar)

    def Update(self, content: dict) :
        if content.get("finished", False) :
            self.buttonTextVar.set(content["name"] + "(已完成)")
            self.buttonWidget.config(state=tk.DISABLED)
        else :
            self.buttonTextVar.set(content["name"])
            self.buttonWidget.config(state=tk.ACTIVE)

        tooltipText = "-----------描述-----------\n"
        tooltipText += content.get("desc", "") + "\n"

        cost = content.get("cost", [])
        if len(cost) > 0 :
            tooltipText += "-----------研究消耗-----------\n"
            for item in cost :
                tooltipText += "{}: {}\n".format(GetEntityDisplayName(item.get("id", "")), item.get("need", 0))

        effects = content.get("effects", [])
        if len(effects) > 0 :
            tooltipText += "-----------效果-----------\n"
            for effect in effects :
                tooltipText += effect + "\n"
        self.buttonTooltipTextVar.set(tooltipText)
        return

    def Research(self, researchId: str) :
        if hasattr(self.gameEngine, "Research") :
            self.gameEngine.Research(researchId)
        return

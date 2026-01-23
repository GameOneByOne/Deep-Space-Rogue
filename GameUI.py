import tkinter as tk
from functools import partial
from Tooltip import Tooltip
from GameBuilding import BuildingType


class ResourceItemUI :
    def __init__(self, root, ) :
        self.resourceCountAndRateVar = tk.StringVar()
        self.resourceLabelWidget = tk.Label(root, textvariable=self.resourceCountAndRateVar, height=1, width=25,  bg="#f0f0f0")
        self.resourceLabelWidget.pack(side=tk.TOP, padx=5, anchor="nw")

    def Update(self, content) :
        resourceTitle = content["name"].ljust(6 - len(content["name"]))
        resourceCountAndLimit = (": {}/{}".format(content["count"], content["limit"])).ljust(10)
        resourceRate = ""
        if (content["rate"] >= 0) :
            resourceRate = "+{:.2f}".format(content["rate"]).rjust(7)
        else :
            resourceRate = "-{:.2f}".format(content["rate"]).rjust(7)

        self.resourceCountAndRateVar.set(resourceTitle + resourceCountAndLimit + resourceRate)
        return


class BuildingItemUI :
    def __init__(self, id, root, gameEngine, gameData) :
        self.gameEngine = gameEngine
        self.gameData = gameData
        self.buttonTextVar = tk.StringVar()
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonWidget = tk.Button(root, textvariable=self.buttonTextVar, height=1, width=10, bg="#f0f0f0", command=partial(self.Build, id))
        self.buttonWidget.pack(side=tk.LEFT, padx=5, anchor="nw")
        Tooltip(self.buttonWidget, self.buttonTooltipTextVar)

    def Update(self, content : dict) :
        # 更新按钮文本

        if content["type"] == BuildingType.TICKABLE :
            self.buttonTextVar.set(content["name"] + "({})".format(content["count"]))
        else :
            self.buttonTextVar.set(content["name"])

        # 更新按钮状态
        self.buttonWidget.config(state=tk.ACTIVE if content["canBuild"] else tk.DISABLED)

        # 更新按钮提示文本
        tooltipText = "-----------描述-----------\n"
        tooltipText += content["description"] + "\n"
        if len(content["buildCostResources"]) > 0 :
            tooltipText += "-----------建筑费用-----------\n"
            for resourceId, resourceCount in content["buildCostResources"].items() :
                tooltipText += (self.gameData.GetItemName(resourceId) + ": {}\n".format(resourceCount))
        resourceSuffix = "/s" if content["type"] == BuildingType.TICKABLE else ""
        if len(content["resourceInput"]) > 0 :
            tooltipText += "-----------资源消耗-----------\n"
            for resourceId, resourceCount in content["resourceInput"].items() :
                tooltipText += (self.gameData.GetItemName(resourceId) + ": {}{}\n".format(resourceCount, resourceSuffix))
        if len(content["resourceOutput"]) > 0 :
            tooltipText += "-----------资源产出-----------\n"
            for resourceId, resourceCount in content["resourceOutput"].items() :
                tooltipText += (self.gameData.GetItemName(resourceId) + ": {}{}\n".format(resourceCount, resourceSuffix))
        self.buttonTooltipTextVar.set(tooltipText)

        return

    def Build(self, buildingId : str) :
        self.gameEngine.Build(buildingId)
        return
    

class ProfessionButtonUI :
    def __init__(self, id, root, gameEngine, canEdit) :
        self.gameEngine = gameEngine
        self.buttonTextVar = tk.StringVar()
        self.buttonFrameWidget= tk.Frame(root, relief="solid", borderwidth=1, width=50, height=30, bg="white")
        self.professionLabelWidget = tk.Label(self.buttonFrameWidget, height=1, width=10, bg="#f0f0f0")
        self.professionLabelWidget.pack(side=tk.LEFT, padx=5)
        
        self.professionAddButtonWidget = tk.Button(self.buttonFrameWidget, text="+", height=1, width=1, bg="#f0f0f0", command=partial(self.Dispatch, id))
        self.professionSubButtonWidget = tk.Button(self.buttonFrameWidget, text="-", height=1, width=1, bg="#f0f0f0", command=partial(self.UnDispatch, id))
        if canEdit :           
            self.professionAddButtonWidget.pack(side=tk.RIGHT)
            self.professionSubButtonWidget.pack(side=tk.RIGHT)
        self.buttonFrameWidget.pack(side=tk.TOP, padx=5, anchor="nw")

    def Update(self, content : dict) :
        self.professionLabelWidget.config(text="{}: {}".format(content["name"], content["count"]))

    def Dispatch(self, professionId : str) :
        self.gameEngine.Dispatch(professionId)
        return

    def UnDispatch(self, professionId : str) :
        self.gameEngine.UnDispatch(professionId)
        return

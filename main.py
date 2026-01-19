import os
import time
import threading
import tkinter as tk
from functools import partial

from Tooltip import Tooltip
from GameData import GameData
from GameEngine import GameEngine, BuildingType

GAME_TITLE = "星际探索 - 文字肉鸽游戏"
GAME_WINDOW_SIZE = "500x500"
GAME_DATA_PATH = "data/data.cfg"
FPS : float = 1 / 60

gGameContinue = True
tickCount = 1.0
gameData = GameData(GAME_DATA_PATH)
gameEngine = GameEngine(gameData)
resourceLabelList = dict()
buildingButtonList = dict()

def GameClose() :
    global gGameContinue
    global mainThread
    global gGameIsWorking
    gGameContinue = False
    root.after(100, root.destroy)

def Build(buildingId : str) :
    gameEngine.Build(buildingId)
    return

def FormatResourceText(resource : dict) :
    resourceTitle = resource["name"].ljust(6 - len(resource["name"]))
    resourceCountAndLimit = (": {}/{}".format(resource["count"], resource["limit"])).ljust(10)
    resourceRate = ""
    if (resource["rate"] >= 0) :
        resourceRate = "+{:.2f}".format(resource["rate"]).rjust(7)
    else :
        resourceRate = "-{:.2f}".format(resource["rate"]).rjust(7)
    return resourceTitle + resourceCountAndLimit + resourceRate

def FormatBuildingText(building : dict) :
    if building["type"] == BuildingType.TICKABLE :
        return building["name"] + "({})".format(building["count"])
    else :
        return building["name"]

def FormatBuildingTooltip(building : dict) :
    tooltipText = "-----------描述-----------\n"
    tooltipText += building["description"] + "\n"
    if len(building["buildCostResources"]) > 0 :
        tooltipText += "-----------建筑费用-----------\n"
        for resourceId, resourceCount in building["buildCostResources"].items() :
            tooltipText += (gameData.GetItemName(resourceId) + ": {}\n".format(resourceCount))

    resourceSuffix = "/s" if building["type"] == BuildingType.TICKABLE else ""
    if len(building["resourceInput"]) > 0 :
        tooltipText += "-----------资源消耗-----------\n"
        for resourceId, resourceCount in building["resourceInput"].items() :
            tooltipText += (gameData.GetItemName(resourceId) + ": {}{}\n".format(resourceCount, resourceSuffix))
    if len(building["resourceOutput"]) > 0 :
        tooltipText += "-----------资源产出-----------\n"
        for resourceId, resourceCount in building["resourceOutput"].items() :
            tooltipText += (gameData.GetItemName(resourceId) + ": {}{}\n".format(resourceCount, resourceSuffix))

        
    return tooltipText

def ShowInfo() :
    global tickCount
    global gGameContinue

    while gGameContinue :
        tickCount += FPS
        if tickCount >= 1.0 :
            gameEngine.Tick()
            tickCount = 0.0
        buildings, resources = gameEngine.Show()

        # 组装资源显示模块
        for resource in resources.values() :
            widget = resourceLabelList.get(resource["id"], None)
            content = FormatResourceText(resource)
            if widget == None :
                resourceLabelList[resource["id"]] = tk.Label(resourceFrame, height=1, width=25,  bg="#f0f0f0")
                resourceLabelList[resource["id"]].pack(side=tk.TOP, padx=5, anchor="nw")
            resourceLabelList[resource["id"]].config(text=content)

        # 组装建筑显示模块
        for building in buildings.values() :
            widget = buildingButtonList.get(building["id"], None)
            buttonText = FormatBuildingText(building)
            tooltipText = FormatBuildingTooltip(building)
            if widget == None :
                buildingButtonList[building["id"]] = tk.Button(buildingFrame, height=1, width=10, bg="#f0f0f0", command=partial(Build, building["id"]))
                Tooltip(buildingButtonList[building["id"]], tooltipText)
                buildingButtonList[building["id"]].pack(side=tk.LEFT, padx=5, anchor="nw")
            buildingButtonList[building["id"]].config(text=buttonText)
        time.sleep(0.016)

root = tk.Tk()
root.title(GAME_TITLE)
root.geometry(GAME_WINDOW_SIZE)
root.protocol("WM_DELETE_WINDOW", GameClose)

# 绘制资源面板
resourceTitleLabel = tk.Label(root, height=1, width=8, text="资源面板", bg="#d32323")
resourceTitleLabel.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
resourceFrame = tk.Frame(root, relief="solid", borderwidth=3, width=400, height=200, bg="white")
resourceFrame.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
resourceFrame.pack_propagate(False)

# 绘制建筑操作面板
buildingTitleLabel = tk.Label(root, height=1, width=8, text="操作面板", bg="#0cebba")
buildingTitleLabel.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
buildingFrame = tk.Frame(root, relief="solid", borderwidth=3, width=400, height=200, bg="white")
buildingFrame.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
buildingFrame.pack_propagate(False)


# 开启后台逻辑线程
mainThread = threading.Thread(target=ShowInfo)
mainThread.start()
root.mainloop()
mainThread.join()

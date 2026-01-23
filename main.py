import os
import time
import threading
import tkinter as tk
from functools import partial

from Tooltip import Tooltip
from GameData import GameData
from GameEngine import GameEngine
from GameUI import ResourceItemUI, BuildingItemUI, ProfessionButtonUI

GAME_TITLE = "星际探索 - 文字肉鸽游戏"
GAME_WINDOW_SIZE = "500x800"
FPS : float = 1 / 60

gGameContinue = True
tickCount = 1.0
gameData = GameData()
gameEngine = GameEngine(gameData)
resourceLabelList = dict()
buildingButtonList = dict()
professionFrameList = dict()

def GameClose() :
    global gGameContinue
    gGameContinue = False
    root.after(100, root.destroy)

def ShowInfo() :
    global tickCount
    global gGameContinue

    while gGameContinue :
        tickCount += FPS
        if tickCount >= 1.0 :
            gameEngine.Tick()
            tickCount = 0.0

        mainInfos, buildings, resources, professions = gameEngine.Show()

        # 更新资源显示模块
        for resource in resources.values() :
            widget = resourceLabelList.get(resource["id"], None)
            if widget == None :
                resourceLabelList[resource["id"]] = ResourceItemUI(resourceFrame)
                resourceLabelList[resource["id"]].Update(resource)
            else :
                widget.Update(resource)

        # 更新建筑显示模块
        for building in buildings.values() :
            widget = buildingButtonList.get(building["id"], None)
            if widget == None :
                buildingButtonList[building["id"]] = BuildingItemUI(building["id"], buildingFrame, gameEngine, gameData)
                buildingButtonList[building["id"]].Update(building)
            else :
                widget.Update(building)

        # 组装职业显示模块
        for profession in professions.values() :
            widget = professionFrameList.get(profession["id"], None)
            if widget == None :
                professionFrameList[profession["id"]] = ProfessionButtonUI(profession["id"], professionFrame, gameEngine, profession["canEdit"])
                professionFrameList[profession["id"]].Update(profession)
            else :
                widget.Update(profession)
        
        # 组装人力显示模块
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

# 绘制人力面板
professionTitleLabel = tk.Label(root, height=1, width=8, text="人力面板", bg="#ff9a00")
professionTitleLabel.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
professionFrame = tk.Frame(root, relief="solid", borderwidth=3, width=400, height=200, bg="white")
professionFrame.pack(side=tk.TOP, fill=tk.X, padx=20, expand=True)
professionFrame.pack_propagate(False)


# 开启后台逻辑线程
mainThread = threading.Thread(target=ShowInfo)
mainThread.start()
root.mainloop()
mainThread.join()

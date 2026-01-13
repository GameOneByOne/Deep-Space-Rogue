import os
import time
import threading
import tkinter as tk
from functools import partial

from GameData import GameData
from GameEngine import GameEngine

GAME_DATA_PATH = "data.cfg"
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
            resourceTitle = resource["name"].ljust(6 - len(resource["name"]))
            resourceCountAndLimit = (": {}/{}".format(resource["count"], resource["limit"])).ljust(10)
            resourceRate = ""
            if (resource["rate"] >= 0) :
                resourceRate = "+{:.2f}".format(resource["rate"]).rjust(7)
            else :
                resourceRate = "-{:.2f}".format(resource["rate"]).rjust(7)
            content = resourceTitle + resourceCountAndLimit + resourceRate
            if widget == None :
                resourceLabelList[resource["id"]] = tk.Label(resourceFrame, height=1, width=25,  bg="#f0f0f0")
                resourceLabelList[resource["id"]].config(text=content)
                resourceLabelList[resource["id"]].pack(side=tk.TOP, padx=5, anchor="nw")
            else :
                resourceLabelList[resource["id"]].config(text=content)

        # 组装建筑显示模块
        for building in buildings.values() :
            widget = buildingButtonList.get(building["id"], None)
            buttonText = building["name"] + "({})".format(building["count"])
            if widget == None :
                buildingButtonList[building["id"]] = tk.Button(buildingFrame, height=1, width=10, text=buttonText, bg="#f0f0f0", command=partial(Build, building["id"]))
                buildingButtonList[building["id"]].pack(side=tk.LEFT, padx=5, anchor="nw")
            else :
                buildingButtonList[building["id"]].config(text=buttonText)
        time.sleep(0.016)

root = tk.Tk()
root.title("星际探索 - 文字肉鸽游戏")
root.geometry("500x500")
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

import os
import time
import threading
import tkinter as tk

from GameEngine import GameEngine
from GameUI import (
    ResourceItemUI,
    BuildingItemUI,
    ProfessionButtonUI,
    ResearchItemUI,
    COLOR_BG,
    COLOR_PANEL,
    COLOR_TEXT,
    COLOR_BORDER,
    FONT_BODY,
)

GAME_TITLE = "星际探索 - 文字肉鸽游戏"
GAME_WINDOW_SIZE = "500x800"
FPS : float = 1 / 60

gGameContinue = True
tickCount = 1.0
gameEngine = GameEngine()
resourceLabelList = dict()
buildingButtonList = dict()
professionFrameList = dict()
researchButtonList = dict()

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

        mainInfos, buildings, resources, professions, researchInfos = gameEngine.Show()

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
                buildingButtonList[building["id"]] = BuildingItemUI(building["id"], buildingFrame, gameEngine)
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

        # 组装研究显示模块
        for research in researchInfos.values() :
            widget = researchButtonList.get(research["id"], None)
            if widget == None :
                researchButtonList[research["id"]] = ResearchItemUI(research["id"], researchFrame, gameEngine)
                researchButtonList[research["id"]].Update(research)
            else :
                widget.Update(research)
        
        # 组装人力显示模块
        time.sleep(0.016)

root = tk.Tk()
root.title(GAME_TITLE)
root.geometry(GAME_WINDOW_SIZE)
root.protocol("WM_DELETE_WINDOW", GameClose)
root.configure(bg=COLOR_BG)

def CreatePanel(title: str, titleColor: str) :
    titleLabel = tk.Label(
        root,
        height=1,
        text=title,
        bg=titleColor,
        fg=COLOR_TEXT,
        font=FONT_BODY,
        pady=4
    )
    titleLabel.pack(side=tk.TOP, fill=tk.X, padx=16, pady=(8, 2))
    panelFrame = tk.Frame(
        root,
        relief="flat",
        borderwidth=0,
        width=460,
        height=165,
        bg=COLOR_PANEL,
        highlightthickness=1,
        highlightbackground=COLOR_BORDER
    )
    panelFrame.pack(side=tk.TOP, fill=tk.X, padx=16, pady=(0, 6), expand=False)
    panelFrame.pack_propagate(False)
    return panelFrame

# 绘制资源面板
resourceFrame = CreatePanel("资源面板", "#1D5D7B")

# 绘制建筑操作面板
buildingFrame = CreatePanel("操作面板", "#2A6F97")

# 绘制人力面板
professionFrame = CreatePanel("人力面板", "#3B7FA6")

# 绘制研究面板
researchFrame = CreatePanel("研究面板", "#4A8BB3")


# 开启后台逻辑线程
mainThread = threading.Thread(target=ShowInfo)
mainThread.start()
root.mainloop()
mainThread.join()

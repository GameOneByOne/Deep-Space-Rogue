import tkinter as tk
from functools import partial
from Tooltip import Tooltip
from GameUtils import GetEntityDisplayName


COLOR_BG = "#0E1A24"
COLOR_PANEL = "#132735"
COLOR_PANEL_ALT = "#173141"
COLOR_TEXT = "#E8F1F8"
COLOR_MUTED = "#9FB3C7"
COLOR_ACCENT_HOVER = "#7AD5FF"
COLOR_BUTTON = "#1E4A63"
COLOR_BUTTON_DISABLED = "#3E5566"
COLOR_BORDER = "#3A6078"
FONT_BODY = ("Consolas", 10)
FONT_MONO = ("Consolas", 9)


class ResourceItemUI :
    def __init__(self, root) :
        self.resourceCountAndRateVar = tk.StringVar()
        self.resourceLabelWidget = tk.Label(
            root,
            textvariable=self.resourceCountAndRateVar,
            height=1,
            width=30,
            bg=COLOR_PANEL_ALT,
            fg=COLOR_TEXT,
            font=FONT_MONO,
            anchor="w",
            padx=8,
            pady=4
        )
        self.resourceLabelWidget.pack(side=tk.TOP, padx=6, pady=2, fill=tk.X, anchor="nw")

    def Update(self, content) :
        resourceTitle = content["name"]
        countText = FormatNumber(content["count"])
        limitText = FormatNumber(content["limit"])
        resourceCountAndLimit = " {}/{}".format(countText, limitText)
        if content["rate"] >= 0 :
            resourceRate = "+{:.2f}".format(content["rate"])
        else :
            resourceRate = "{:.2f}".format(content["rate"])
        self.resourceCountAndRateVar.set("{}{}    {}".format(resourceTitle, resourceCountAndLimit, resourceRate))
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
        self.buttonWidget = tk.Button(
            root,
            textvariable=self.buttonTextVar,
            height=1,
            width=14,
            bg=COLOR_BUTTON,
            fg=COLOR_TEXT,
            activebackground=COLOR_ACCENT_HOVER,
            activeforeground="#0B1923",
            disabledforeground=COLOR_MUTED,
            relief="flat",
            font=FONT_BODY,
            command=partial(self.Build, id)
        )
        self.buttonWidget.pack(side=tk.LEFT, padx=6, pady=4, anchor="nw")
        Tooltip(self.buttonWidget, self.buttonTooltipTextVar)

    def Update(self, content : dict) :
        if content["count"] != 0 :
            self.buttonTextVar.set(content["name"] + "({})".format(content["count"]))
        else :
            self.buttonTextVar.set(content["name"])

        self.buttonWidget.config(state=tk.ACTIVE if content["canBuild"] else tk.DISABLED)

        tooltipText = "-----------描述-----------\n"
        tooltipText += content["desc"] + "\n"
        cost = content.get("costDesc", [])
        if len(cost) > 0 :
            tooltipText += "-----------建造消耗-----------\n"
            for item in cost :
                tooltipText += "{}\n".format(item)
        tooltipText += "-----------效果-----------\n"
        for effect in content["effectsDesc"] :
            tooltipText += effect + "\n"
        self.buttonTooltipTextVar.set(tooltipText)
        return

    def Build(self, buildingId : str) :
        self.gameEngine.Build(buildingId)
        return


class ProfessionButtonUI :
    def __init__(self, id, root, gameEngine, canEdit) :
        self.gameEngine = gameEngine
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonFrameWidget = tk.Frame(
            root,
            relief="solid",
            borderwidth=1,
            width=60,
            height=34,
            bg=COLOR_PANEL_ALT,
            highlightthickness=1,
            highlightbackground=COLOR_BORDER
        )
        self.professionLabelWidget = tk.Label(
            self.buttonFrameWidget,
            height=1,
            width=14,
            bg=COLOR_PANEL_ALT,
            fg=COLOR_TEXT,
            font=FONT_BODY
        )
        self.professionLabelWidget.pack(side=tk.LEFT, padx=6)

        self.professionAddButtonWidget = tk.Button(
            self.buttonFrameWidget,
            text="+",
            height=1,
            width=2,
            bg=COLOR_BUTTON,
            fg=COLOR_TEXT,
            activebackground=COLOR_ACCENT_HOVER,
            relief="flat",
            command=partial(self.Dispatch, "P_IDLE", id)
        )
        self.professionSubButtonWidget = tk.Button(
            self.buttonFrameWidget,
            text="-",
            height=1,
            width=2,
            bg=COLOR_BUTTON,
            fg=COLOR_TEXT,
            activebackground=COLOR_ACCENT_HOVER,
            relief="flat",
            command=partial(self.Dispatch, id, "P_IDLE")
        )
        if canEdit :
            self.professionAddButtonWidget.pack(side=tk.RIGHT)
            self.professionSubButtonWidget.pack(side=tk.RIGHT)
        self.buttonFrameWidget.pack(side=tk.TOP, padx=6, pady=3, anchor="nw")

        Tooltip(self.buttonFrameWidget, self.buttonTooltipTextVar)
        Tooltip(self.professionLabelWidget, self.buttonTooltipTextVar)
        if canEdit :
            Tooltip(self.professionAddButtonWidget, self.buttonTooltipTextVar)
            Tooltip(self.professionSubButtonWidget, self.buttonTooltipTextVar)

    def Update(self, content : dict) :
        if content["limit"] < 0 :
            self.professionLabelWidget.config(text="{}: {}".format(content["name"], content["count"]))
        else :
            self.professionLabelWidget.config(text="{}: {}/{}".format(content["name"], content["count"], content["limit"]))

        tooltipText = "-----------描述-----------\n"
        tooltipText += content["desc"] + "\n"
        tooltipText += "-----------效果-----------\n"
        if len(content["effectsDesc"]) > 0 :
            for effect in content["effectsDesc"] :
                tooltipText += effect + "\n"
        else :
            tooltipText += "无\n"
        self.buttonTooltipTextVar.set(tooltipText)
        return

    def Dispatch(self, fromnProfessionId : str, toProfessionId : str) :
        self.gameEngine.Dispatch(fromnProfessionId, toProfessionId)
        return


class ResearchItemUI :
    def __init__(self, id, root, gameEngine) :
        self.gameEngine = gameEngine
        self.buttonTextVar = tk.StringVar()
        self.buttonTooltipTextVar = tk.StringVar()
        self.buttonWidget = tk.Button(
            root,
            textvariable=self.buttonTextVar,
            height=1,
            width=14,
            bg=COLOR_BUTTON,
            fg=COLOR_TEXT,
            activebackground=COLOR_ACCENT_HOVER,
            activeforeground="#0B1923",
            disabledforeground=COLOR_MUTED,
            relief="flat",
            font=FONT_BODY,
            command=partial(self.Research, id)
        )
        self.buttonWidget.pack(side=tk.LEFT, padx=6, pady=4, anchor="nw")
        Tooltip(self.buttonWidget, self.buttonTooltipTextVar)

    def Update(self, content: dict) :
        if content.get("finished", False) :
            self.buttonTextVar.set(content["name"] + "(已完成)")
            self.buttonWidget.config(state=tk.DISABLED, bg=COLOR_BUTTON_DISABLED)
        else :
            self.buttonTextVar.set(content["name"])
            self.buttonWidget.config(state=tk.ACTIVE, bg=COLOR_BUTTON)

        tooltipText = "-----------描述-----------\n"
        tooltipText += content.get("desc", "") + "\n"
        cost = content.get("costDesc", [])
        if len(cost) > 0 :
            tooltipText += "-----------研究消耗-----------\n"
            for item in cost :
                tooltipText += "{\n".format(item)
        effects = content.get("effectsDesc", [])
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

import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.id = None
        self.x = self.y = 0
        
        # 绑定事件
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<ButtonPress>", self.on_leave)
    
    def on_enter(self, event=None):
        self.schedule()
    
    def on_leave(self, event=None):
        self.unschedule()
        self.hide_tooltip()
    
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(100, self.show_tooltip)
    
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
    
    def show_tooltip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + int(self.widget.winfo_width() / 2)
        y += self.widget.winfo_rooty() + self.widget.winfo_height()
        
        # 创建tooltip窗口
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        
        # 创建包含tooltip文本的标签
        label = tk.Label(tw, textvariable=self.text, justify='left',background="#ffffe0",relief='solid',borderwidth=1,font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    
    def hide_tooltip(self):
        tw = self.tooltip_window
        self.tooltip_window = None
        if tw:
            tw.destroy()
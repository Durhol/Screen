"""/////////////////////////////"""

from tkinter import *
import keyboard
from random import *

"""/////////////////////////////"""

keyboard.block_key('windows')
keyboard.block_key('shift')
keyboard.block_key('ctrl')
keyboard.block_key('alt')

"""/////////////////////////////"""

root = Tk()
root.title("Screen")
root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
png = PhotoImage(file="image.png")
ScreenWidth = root.winfo_screenwidth()
ScreenHeight = root.winfo_screenheight()

"""/////////////////////////////"""

PNGScreen = Canvas(root, width=ScreenWidth, height=ScreenHeight)
PNGScreen.pack()
PNG = PNGScreen.create_image(ScreenWidth // 2, ScreenHeight // 2, image=png)

"""/////////////////////////////"""

def Moving():
    mx = randint(-100, 100)
    my = randint(-100, 100)
    PNGScreen.move(PNG, mx, my)
    root.after(100, Moving)

"""/////////////////////////////"""

Moving()
root.mainloop()

 
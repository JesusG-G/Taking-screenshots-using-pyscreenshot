import pyautogui
import pyscreenshot
import tkinter as tk
import time as time
import keyboard as keyboard
from tkinter.filedialog import *


def on_button_click(event):
    global x0, y0, rectangle, box_canva
    x0 = event.x
    y0 = event.y
    
    rectangle = box_canva.create_rectangle(x0,y0,1,1,outline='red')


def on_button_release(event):
    global x0,y0,a
    x1 = event.x
    y1 = event.y
    screenshoot = pyscreenshot.grab(bbox=(x0,y0,x1,y1))
    a = 2
    save_path = asksaveasfilename()
    screenshoot.save(save_path+"_screenshot.png")
    screenshoot.show()

def on_move_press(event):
    global rectangle, box_canva
    curX = box_canva.canvasx(event.x)
    curY = box_canva.canvasy(event.y)
    box_canva.coords(rectangle, x0, y0, curX, curY)

def take_full_screenshot():
    root.iconify()
    screenshoot = pyscreenshot.grab()
    save_path = asksaveasfilename()
    screenshoot.save(save_path+"_screenshot.png")
    screenshoot.show()
    root.deiconify()

def box_screenshot():
    root.iconify()
    global a, box_canva
    cursor_position = tk.Tk()
    weight = 200
    height = 40
    a = 1
    weight_screen = cursor_position.winfo_screenwidth()
    height_screen = cursor_position.winfo_screenheight()
    mouse_text = tk.Text(cursor_position,font=10)
    background_window = tk.Tk()
    background_window.attributes("-fullscreen",True)
    background_window.config(bg='', cursor='cross') 
    box_canva = tk.Canvas(background_window)

    while True:
        x,y = pyautogui.position()
        posStrx = str(x).rjust(4)
        posStry = str(y).rjust(4)
        mouse_position = f"X: {posStrx} Y: {posStry}"
        mouse_text.insert(tk.INSERT, mouse_position)
        mouse_text.pack()
        background_window.bind("<Button-1>", on_button_click)
        background_window.bind("<B1-Motion>", on_move_press)
        background_window.bind("<ButtonRelease-1>", on_button_release)
        time.sleep(0.0005)
        x = int(posStrx) + 15
        y = int(posStry) + 15
        
        if keyboard.is_pressed('esc'):
            a = 2

        if a==1:
            cursor_position.wm_overrideredirect(1)
            if 0<x<=(6*weight_screen/8) and 0<y<=(7*height_screen/8):
                cursor_position.geometry('%dx%d+%d+%d' %(weight, height, x, y))
            elif (6*weight_screen/8)<=x and 0<y<=(7*height_screen/8):
                cursor_position.geometry('%dx%d+%d+%d' %(weight, height, (x-(weight+30+10)), y))
            elif 0<x<=(6*weight_screen/8) and (7*height_screen/8)<=y:
                cursor_position.geometry('%dx%d+%d+%d' %(weight, height, x, (y-(height+30+10))))
            else:
                cursor_position.geometry('%dx%d+%d+%d' %(weight, height, (x-(weight+30+10)), (y-(height+30+10))))
        
        cursor_position.update()
        mouse_text.delete(1.0,tk.END)
        mouse_text.pack()

            
        if a==2:
            break

    cursor_position.destroy()
    background_window.destroy()
    root.deiconify()




root = tk.Tk()
x0 = 0
y0 = 0
x1 = 0
y1 = 0 
a = 1
rectangle = None
box_canva = None
canvas_1 = tk.Canvas(root,width=300, height=300,)
canvas_1.pack()

screenshot_button = tk.Button(text="Take Full Screenshot", command=take_full_screenshot, font=10)
box_screenshoot_button = tk.Button(text="Capture a region", command=box_screenshot,font=10)
canvas_1.create_window(150,150,window=screenshot_button)
canvas_1.create_window(150,200,window=box_screenshoot_button)


root.mainloop()
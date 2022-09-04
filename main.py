import pyautogui as pt 
from time import sleep
import pyperclip
import random
import string
import pyjokes
from tkinter import Tk
import pyperclip
from keyboard import press




sleep(1)

pos1 = pt.locateOnScreen("new.png" ,confidence=.6)

x = pos1[0]
y = pos1[1]


def new_massage():
    global x, y
    
    postion = pt.locateOnScreen("new.png" ,confidence=.6)
    x = postion[0]
    y = postion[1]
    pt.moveTo(x, y, duration=.01)
    pt.moveTo(x -100 , y  , duration=.001)
    pt.click()
def copy_massage():
    global x, y
    postion = pt.locateOnScreen("read.png" ,confidence=.6)
    x = postion[0]
    y = postion[1]
    pt.moveTo(x, y, duration=.001)
    pt.moveTo(x + 180 , y - 65 , duration=.001)
    pt.tripleClick()
    pt.hotkey("ctrlleft", "c")
    message = Tk().clipboard_get()
    

    
    
    return message 
    
    
def replay(msg):
    global x, y 
    postion = pt.locateOnScreen("read.png" ,confidence=.6)
    x = postion[0]#
    y = postion[1]
    pt.moveTo(x + 200, y +20, duration=.001)
    pt.click()
    print("ok")
    pt.typewrite(msg, interval=.00001)
    print("okkkkk")
        
    
    pt.press('enter')
    
    pyperclip.copy("nonnn")
    print("yes yse")
    
while True:  

    new_massage()
    copy_massage()
    print(copy_massage())
    if(copy_massage() == "joke"):
     replay(pyjokes.get_joke(language="en", category="neutral"))
     
    if(copy_massage() == "stop stop"):
        print("off")
        break

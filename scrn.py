import time 
from kbr import presser
from stf import clr
import os
cmnd = clr()
def screen_config(speed):
    height = 0
    width = 0
    while True:
        time.sleep(speed)
        d = presser([' ',' '])
        if 'q' in d:
            return height,width
        if 'u' in d:
            height += -1
        if 'd' in d:
            height += 1
        if 'r' in d:
            width += 1
        if 'l' in d:
            width += -1
        text = sPrint(height,width)
        text += "\nUse w,s,d,a to change the size of the screen, press q when the screen is at the wanted size"
        os.system(cmnd)
        print (text)
def sPrint(height,width):
    text = ""
    text += "-" * width
    text += "\n"
    for r in range(height):
        text += "|"
        for c in range(width):
            text += " "
        text += "|\n"
    for i in range(width):
        text += "-"
    return text

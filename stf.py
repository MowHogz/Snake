import platform 
import os 
def clr():
    so = platform.system()
    if so == "Linux":
        cmnd = "clear"
    elif so == "Windows":
        cmnd = "cls"
    else:
        cmnd = ""
    return cmnd
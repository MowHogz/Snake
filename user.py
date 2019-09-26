from stf import clr
import os
cmnd = clr()
def Printer(matrix,score):
    text = ""
    text += "Score: " + str(score) + "\n"
    for row in matrix:
        for unit in row:
            text += unit
        text += "\n"
    
    os.system(cmnd)
    print (text)

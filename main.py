import time
from kbr import press
from mat import creator
from food import gen_food
from snake import snake
import os
height = 20
width = 20
matrix = creator(height,width)

speed = 10

amounts_of_foods = 3
for i in range(amounts_of_foods):
    gen_food(matrix,height,width)
snook = snake()
d = 'd'
for i in range(width):
    matrix[0][i] = 'X'


def Printer(matrix,height,width):
    text = ""
    for row in matrix:
        text += "\n"
        for unit in row:
            text += unit
    os.system('cls')
    print (text) 

while True:
    for i in range(25):
        time.sleep(0.005)
        d = press(d)
    if not snook.move(matrix,height,width,d):
        print("Your snake Died, So shall you!!!")
        break
    Printer(matrix,height,width)



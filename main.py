import time
from kbr import press
from mat import creator
from food import gen_food
from snake import snake
import os
height = 60
width = 60
matrix = creator(height,width)

speed = 10
players = 3
players = int(input("Enter the number of players: "))
amounts_of_foods = 30
for i in range(amounts_of_foods):
    gen_food(matrix,height,width)
snook = snake(0,0)
print ("Player 1 (top player) uses WSDA controls")
if players > 1:
    print ("Player 2 (second from top) uses IKLJ controls")
    snack = snake(5,0)
    if players > 2:
        print ("Player 3 (3rd from top) uses TGHF controls")
        sneak = snake(10,0)
d = []
"""
for i in range(width):
    matrix[0][i] = 'X'

for i in range(width):
    matrix[5][i] = 'X'

"""
def con1(d,o):
    list1 = ['w','s','d','a']
    list2 = ['u','d','r','l']
    for l in range(len(list1)):
        if list1[l] in d:
            return list2[l]
    return o
def con2(d,o):
    list1 = ['i','k','l','j']
    list2 = ['u','d','r','l']
    for l in range(len(list1)):
        if list1[l] in d:
            return list2[l]
    return o
def con3(d,o):
    list1 = ['t','g','h','f']
    list2 = ['u','d','r','l']
    for l in range(len(list1)):
        if list1[l] in d:
            return list2[l]
    return o
def Printer(matrix,height,width):
    text = ""
    for row in matrix:
        text += "\n"
        for unit in row:
            text += unit
    os.system('cls')
    print (text) 
a = 'r'
b = 'r'
c = 'r'
goon = True
raw_input("Press Enter to start")
for i in range(3):
    os.system('cls')
    print (str("\n" * 3) + str(' ' * int(width/2)) + str(3-i) )
    time.sleep(1)
os.system('cls')
print (str("\n" * 3) + str(' ' * int(width/2)) + "Go!" )
time.sleep(1)
while True:
    d = []
    for i in range(25):
        time.sleep(0.005)
        d = press(d)
    a = con1(d,a)
    if not snook.move(matrix,height,width,a):
        print("Snake A Died, So shall you!!!")
        snook.kill(matrix)
        if goon: 
            snook = snake(0,0)
            a = 'r'
        else: break
    if players > 1:
        b = con2(d,b)
        if not snack.move(matrix,height,width,b):
            print("Snake B Died, So shall you!!!")
            snack.kill(matrix)
            if goon: 
                snack = snake(5,0)
                b = 'r'
            else: break
        if players > 2:
            c = con3(d,c)
            if not sneak.move(matrix,height,width,c):
                print("Snake B Died, So shall you!!!")
                sneak.kill(matrix)
                if goon:
                    sneak = snake(10,0)
                    c = 'r'
                else: break
        
    Printer(matrix,height,width)
    print ("a: {} b:{}".format(a,b))



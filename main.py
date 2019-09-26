from kbr import press
import time 
from brd import matrix_cre
from game import gen_food,mover
from user import Printer
from scrn import screen_config
height = 50 
width = 20 
speed = 0.01
height,width = screen_config(speed)
num_food = 250
matrix = matrix_cre(height,width)
for i in range(num_food):
    gen_food(matrix,height,width)
snake = [[1,1],[0,1]]
direc = 'd'
gaming = True


while gaming:
    for i in range(25):
        time.sleep(speed)
        direc = press(direc)
    print (snake)
    if not mover(matrix,snake,direc,height,width):
        gaming = False
    Printer(matrix,len(snake))
    
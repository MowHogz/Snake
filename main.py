import time 
import random
import keyboard
import os
import msvcrt 
from user import con, Input
def convert(height,width,snake,food):
	matrix = []
	for row in range(height):
		matrix.append([])
		for column in range(width):
			matrix[row].append(" ")

	for unit in snake[:len(snake)-1]:
		matrix[unit[1]][unit[0]] = unit[2]
	unit = snake[len(snake)-1]
	matrix[unit[1]][unit[0]] = "O"
	matrix[food[1]][food[0]] = "X"
	return matrix
	
char = " "
word = ""
brd = []
board = ""
def gen_food(brd,height,width):
	x = random.randint(0,width-1)
	y = random.randint(0,height-1)
	if brd[y][x] == " ":
		return [x,y]
	else:
		return gen_food(brd,height,width)



def create(text):
	print (text)
	return msvcrt.getch()

moves = [0]*4
moves[0] = create("up")
moves[1] = create("down")
moves[2] = create("right")
moves[3] = create("left")

head = [0,0]
height = 10#Input("Please enter the height of the board: ")
width = 10#Input("Please enter the width of the board: ")
brd = []
for row in range(height):
	brd.append([])
	for column in range(width):
		brd[row].append(" ")
snake = [[0,0]]
def move(brd,head,d,moves,height,width,snake,food): #brd - board, head - location, d - direction; char, moves - value of every char; in which direction every char moves, height, width.
	print (head )
	print (food)
	head = head[:2]
	if keyboard.is_pressed("w"):#if moving up
		head,food = move_up(head,brd,food,snake)
		return head,food,"U"
	elif keyboard.is_pressed("s"):#down
		head,food = move_down(head,brd,food,snake)
		return head,food,"D"
	elif keyboard.is_pressed("d"):#right
		head,food = move_right(head,brd,food,snake)
		return head,food,"R"
	elif keyboard.is_pressed("a"):#left
		head,food = move_left(head,brd,food,snake)
		return head,food,"L"
	elif d == "U":
		head,food =  move_up(head,brd,food,snake)
		return head,food,"U"
	elif d == "D":
		head,food =  move_down(head,brd,food,snake)
		return head,food,"D"
	elif d == "R":
		head,food =  move_right(head,brd,food,snake)
		return head,food,"R"
	elif d == "L":
		head,food =  move_left(head,brd,food,snake)
		return head,food,"L"
def move_up(head,brd,food,snake):
	if head[1]>0:#and there is room to go up 
		head[1] += -1#move head to new location 
		return mover(head,brd,food,snake)
	else:
		return False		

def move_down(head,brd,food,snake):
	if head[1]<height-1:
		head[1] += 1
		return mover(head,brd,food,snake)
	else:
		return False		

def move_right(head,brd,food,snake):
	if head[0]<width-1:
		head[0] += 1
		return mover(head,brd,food,snake)
	else:
		return False		

def move_left(head,brd,food,snake):
	if head[0]>0:
		head[0] += -1
		return mover(head,brd,food,snake)
	else:
		return False
def mover(head,brd,food,snake):#returns the consequences of moving 
	if brd[head[1]][head[0]] != " ":
		if brd[head[1]][head[0]] != "X":
			return False
		else:
			food = gen_food(brd,height,width)
	else:
		snake.pop(0) 
	head += "-"
	snake.append(head)
	return head,food

food = gen_food(brd,height,width)
convert(height,width,snake,food)

d = "D"
while True:
	
	time.sleep(0.5)
	head,food,d = move(brd,head,d,moves,height,width,snake,food)
	
	#print ("Game Over!")
	#	break
	brd = convert(height,width,snake,food)
	print (con(brd))
	print("wow")
	#os.system("cls")
	
print ("all done")
import time 
import random
import keyboard
import os
import msvcrt 
from user import con, Input
from bordm import convert
from game import gen_food
head = [0,2]
height = 30#Input("Please enter the height of the board: ")
width = 30#Input("Please enter the width of the board: ")
brd = []
snake = [[0,0,'|'],[0,1,'|'],[0,2,'|']]
	
char = " "
word = ""
brd = []
board = ""
moves = [0]*4
"""
def create(text):
	print (text)
	return msvcrt.getch()
moves[0] = create("up")
moves[1] = create("down")
moves[2] = create("right")
moves[3] = create("left")
"""





for row in range(height):
	brd.append([])
	for column in range(width):
		brd[row].append(" ")
	#print (head )
	#print (food)
def move(brd,head,d,moves,height,width,snake,food): #brd - board, head - location, d - direction; char, moves - value of every char; in which direction every char moves, height, width.
	head = head[:2]
	if d == "U":
		head,food =  move_up(head,brd,food,snake)
		return head,food,d
	elif d == "D":
		head,food =  move_down(head,brd,food,snake)
		return head,food,d
	elif d == "R":
		head,food =  move_right(head,brd,food,snake)
		return head,food,d
	elif d == "L":
		head,food =  move_left(head,brd,food,snake)
		return head,food,d
def move_up(head,brd,food,snake):
	if head[1]>0:#and there is room to go up 
		head[1] += -1#move head to new location 
		head += "|"
		return mover(head,brd,food,snake)
	else:
		return False		

def move_down(head,brd,food,snake):
	if head[1]<height-1:
		head[1] += 1
		head += "|"
		return mover(head,brd,food,snake)
	else:
		return False		

def move_right(head,brd,food,snake):
	if head[0]<width-1:
		head[0] += 1
		head += "-"
		return mover(head,brd,food,snake)
	else:
		return False		

def move_left(head,brd,food,snake):
	if head[0]>0:
		head[0] += -1
		head += "-"
		return mover(head,brd,food,snake)
	else:
		return False
def mover(head,brd,food,snake):#returns the consequences of moving 
	if brd[head[1]][head[0]] != " ":
		if brd[head[1]][head[0]] != "X":
			return False
		else:
			food[food.index(head[:2])] = gen_food(brd,height,width)
	else:
		snake.pop(0) 
	snake.append(head)
	return head,food
def press(d):#program changes direction if a direction is pressed 
	if keyboard.is_pressed("w"):
		d = "U"
	elif keyboard.is_pressed("s"):
		d = "D"
	elif keyboard.is_pressed("d"):
		d = "R"
	elif keyboard.is_pressed("a"):
		d = "L"
	return d
food_n = 40
food = []
for i in range(food_n):
	food.append(gen_food(brd,height,width))
convert(height,width,snake,food)
speed = Input("Please Enter the speed of the snake:")#500
d = "D"
while True:
	
	#print (snake)
	for i in range(speed):
		
		d = press(d)
		if keyboard.is_pressed("r"):
			speed = Input("Please Enter the speed (1-10 recommended):")
	os.system("cls")
	#print (speed/100)
	try: head,food,d = move(brd,head,d,moves,height,width,snake,food)
	except:
		print ("head:{}\n d:{}\n moves:{}\n heigth:{}\n width:{}\n snake:{}\n food:{}\n").format(head,d,moves,height,width,snake,food)
		print (con(brd))
		break
	#print ("Game Over!")
	#	break
	brd = convert(height,width,snake,food)
	print (con(brd))
	#print("wow")
	
print ("all done")
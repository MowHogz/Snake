import os
import msvcrt 
from user import con, Input
def convert(height,width,snake):
	matrix = []
	for row in range(height):
		matrix.append([])
		for column in range(width):
			matrix[row].append(" ")

	for unit in snake[:len(snake)-2]:
		matrix[unit[1]][unit[0]] = unit[2]
	unit = snake[len(snake)-1]
	matrix[unit[1]][unit[0]] = "O"
	return matrix
	
char = " "
word = ""
brd = []
board = ""


def create(text):
	print (text)
	return msvcrt.getch()
moves = [0]*4
moves[0] = create("up")
moves[1] = create("down")
moves[2] = create("right")
moves[3] = create("left")

head = [0,0]
height = Input("Please enter the height of the board: ")
width = Input("Please enter the width of the board: ")
brd = []
for row in range(height):
	brd.append([])
	for column in range(width):
		brd[row].append(" ")
snake = [[0,0]]
def move(brd,head,d,moves,height,width,snake): #brd - board, head - location, d - direction; char, moves - value of every char; in which direction every char moves, height, width.
	if d == moves[0]:#if moving up
		if head[1]>0:#and there is room to go up 
			head[1] += -1#move head to new location 
			if brd[head[1]][head[0]] != " ":#if the snake didn't go into an empty space
				if brd[head[1]][head[0]] != "X":#the space wasn't food
					return False
				else:
					
					pass
			else:
				snake.pop(0) #cut off the last piece of the snake 
			head += "|"
			snake.append(head)
		else:
			return False		
	elif d == moves[1]:#down
		if head[1]<height-1:
			head[1] += 1
			if brd[head[1]][head[0]] != " ":
				if brd[head[1]][head[0]] != "X":
					return False
				else:
					pass
			else:
				snake.pop(0) 
			head += "|"
			snake.append(head)
		else:
			return False		

	elif d == moves[2]:#right
		if head[0]<width-1:
			head[0] += 1
			if brd[head[1]][head[0]] != " ":
				if brd[head[1]][head[0]] != "X":
					return False
				else:

					pass
			else:
				snake.pop(0) 
			head += "-"
			snake.append(head)
		else:
			return False		
	
	elif d == moves[3]:#left
		if head[0]>0:
			head[0] += -1
			if brd[head[1]][head[0]] != " ":
				if brd[head[1]][head[0]] != "X":
					return False
				else:
					pass
			else:
				snake.pop(0) 
			head += "-"
			snake.append(head)
		else:
			return False
	return head
while char != ".":
	head = move(brd,head,char,moves,height,width,snake)
	if head == False:
		print ("Game Over!")
		break
	print (con(convert(height,width,snake)))
	
	#os.system("cls")
	char = msvcrt.getch()
print ("all done")
import random 
def gen_food(brd,height,width):
	x = random.randint(0,width-1)
	y = random.randint(0,height-1)
	if brd[y][x] == " ":
		return [x,y]
	else:
		return gen_food(brd,height,width)

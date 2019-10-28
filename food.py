import random 
def gen_food(matrix,height,width):
    y = random.randint(0,height-1)
    x = random.randint(0,width-1)
    if matrix[y][x] == ' ':
        matrix[y][x] = 'X'
        return [y,x]
    else:
        return gen_food(matrix,height,width)
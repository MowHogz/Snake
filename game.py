from random import randint
def gen_food(matrix,height,width):#generates food and puts it in the board 
    x = randint(0,width) #width and height instead of -1 because there is an extra row (for the '|')
    y = randint(0,height)
    if matrix[y][x] == ' ':
        matrix[y][x] = '*'
    else:
        gen_food(matrix,height,width)
def mover(matrix,snake,direc,height,width):
    print (snake)
    ohead = snake[0]
    if direc == 'u':
        matrix[ohead[0]][ohead[1]] = '|'
        next = [ohead[0]-1,ohead[1]]
    elif direc == 'd':
        matrix[ohead[0]][ohead[1]] = '|'
        next = [ohead[0]+1,ohead[1]]
    elif direc == 'r':
        matrix[ohead[0]][ohead[1]] = '-'
        next = [ohead[0],ohead[1]+1]
    elif direc == 'l':
        matrix[ohead[0]][ohead[1]] = '-'
        next = [ohead[0],ohead[1]-1]
    
    try:
        if matrix[next[0]][next[1]] == '*':#if eats food
            gen_food(matrix,height,width)
            pass
        elif matrix[next[0]][next[1]] == ' ':
            h = snake.pop()
            print(h)
            matrix[h[0]][h[1]] = ' ' #removes the back of the snake from the snake and from the board
        elif next in snake:
            print ("You hit yourself")
            return False
        else:
            print("You hit a wall")
            return False
        #add head to snake and to the board     
        matrix[next[0]][next[1]] = 'O'
        snake.insert(0,next)
        return True
    except:
        print("you went out of the border")
        return False

    
def remover(loc):#gets a location [y,x] and removes it from the board (replaces it with ' ')
    matrix[loc[0]][loc[1]] = ' '
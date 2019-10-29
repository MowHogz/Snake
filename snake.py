import time 
from food import gen_food
class snake():
    def __init__(self,y,x):
        self.body = [[y,x]]
        self.d = 'r'
    def key(self,key_press):
        if key_press == ['b']:
            self.d = [self.d[0],'b']
        elif not key_press == []:
            self.d = key_press
    def move(self,matrix,height,width,d):
        #this part of the function moves the head one space forward 
        self.key(d)
        print (self.d)

        if 'b' in self.d and len(self.body) > 3:
            print ("boosting")
            self.remove_tail(matrix)
            self.d.remove('b')
            self.move(matrix,height,width,self.d)
        if 'r' in self.d:
            self.right(matrix)
        elif 'l' in self.d:
            self.left(matrix)
        elif 'u' in self.d:
            self.up(matrix)
        elif 'd' in self.d:
            self.down(matrix)
        
        head = self.body[0]

        if head[0] < 0 or head[0] >= height or head[1] < 0 or head[1] >= width:
            print("You knocked into a wall")
            return False
        #if going into nowhere kill tail 
        if matrix[head[0]][head[1]] == ' ':
            tail = self.body.pop()
            remove(matrix,tail)
        elif matrix[head[0]][head[1]] == 'X':

            while True:
                if not head == gen_food(matrix,height,width):
                    break
        else:
            return False
        insert(matrix,head,'O')
        return True
        
        #if location of head is ' ' - nothing kill, one piece of the tail off (kill piece off of board and off snake )
        #if location is snake return False 
        #if location is food don't kill last piece 
        #give the old head the new shape it got 
        #insert head 

    def remove_tail(self,matrix):
        tail = self.body.pop()
        remove(matrix,tail)
    def right(self,matrix):
        #mark (old) head 
        head = self.body[0]

        #replace the head with a body part in the matrix 
        insert(matrix,head,'-')

        #insert location of new head into body
        self.body.insert(0, [head[0] , head[1]+1] )

    def left(self,matrix):
        head = self.body[0]
        insert(matrix,head,'-')
        self.body.insert(0, [head[0] , head[1]-1] )

    def up(self,matrix):
        head = self.body[0]
        insert(matrix,head,'|')
        self.body.insert(0, [head[0] - 1 , head[1] ] )
        
    def down(self,matrix):
        head = self.body[0]
        insert(matrix,head,'|')
        self.body.insert(0, [head[0] + 1 , head[1] ] )
    def kill(self,matrix):
        for i in self.body:
            remove(matrix,i)

def insert(matrix,loc,char):
    matrix[loc[0]][loc[1]] = char

def remove(matrix,loc):
    try:
        matrix[loc[0]][loc[1]] = ' '
    except:
        return False
    
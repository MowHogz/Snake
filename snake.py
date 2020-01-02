from space import unit,space
#snake is the snake on the board 
#snake.body is the list of of the unit objects which the snake is made of 
#snake.keys are the keys that have been pressed but not yet processed (reset every frame) - for the game object to mess with 
#self.y - y axis
#self.x - x axis
#grow how much extra/less the snake should grow 
# 
#move() function that moves the snake every frame  
class snake():
    def __init__(self,height,width,game):
        self.game = game
        self.body = [] #the first item will be the tail, and the last item will be the head 
        self.body.append(unit('O',height,width,game))
        self.direction = 'd'#
        self.keys = []
        self.y = height
        self.x = width 
        self.grow = 0 #if the tail should grow/shrink not like usual (a positive number makes the tail stay longer, a negative number makes the tail shrink faster)
    def director(self): #updates the direction value (u,d,r,l) (can be more than one)
        new_direction = []
        
        for l in ['u','d','r','l']:
            if l in self.keys:
                new_direction.append(l)
        self.keys = []
        if new_direction == []:     
            return False
        
        else:                   #if there has been new key input detected, update the self.direction with the new direction
            self.direction = new_direction
        

    def move(self):
        self.director()     #updates the .direction with the direction the snake should be moving 
        self.move_head()    #moves the snakes head in the direction the snake should be moving 
        self.move_tail()    #cuts of 0,-1,-2 off the snake's tail based on the situation (.grow)
    def move_head(self): #moves head one space forward (and changes the 'emoji' of the second space)
        t = "" #look for second piece (old head)
 
        if 'u' in self.direction:       #up 
            self.y -= 1
            if 'r' in self.direction:
                t = "/"
            elif 'l' in self.direction:
                t = "\\"

        elif 'd' in self.direction:     #down
            self.y += 1
            if 'r' in self.direction:
                t = "\\"
            elif 'l' in self.direction:
                t = "/"
        else:
            t = "-"  # - moving right or left 

        if 'r' in self.direction:       #right
            self.x += 1

        elif 'l' in self.direction:     #left
            self.x -= 1

        else:
            t = '|'  # | moving up or down 
        self.body[len(self.body)-1].t = t
        self.body.append(unit('O',self.y,self.x, self.game))
    
    def move_tail(self):    #moves tail 
        if self.grow > 0:       # if tail should grow faster 
                                # don't shrink
            self.grow -= 1      # grow --
            return 0
        else:                   #if tail should shrink
            self.cut_tail()     # shrink tail
            if self.grow < 0:   # if tail should shrink extra 
                self.cut_tail() # shrink one extra time 
                self.grow += 1  # count that shrink
            else: pass
    def cut_tail(self):     #removes the snake's tail safely (with filling in the tile in the game's matrix)
        self.body[0].replace(space())
        self.body.pop(0)

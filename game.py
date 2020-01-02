import os 
from snake import snake 
from space import space
#map is a matrix of spaces (object)
#.snake is the object snake (the main snake in the game - so far there is only one snake)
#.frame run one frame 
class game():
    def __init__(self,height,width):
        self.map = create_matrix(height,width)
        self.keys = []
        #saving the height and width of the matrix
        self.height = height
        self.width  = width 
        self.snake = snake(1,1,self)
    
    def frame(self):
        self.snake.move()
        self.printer()

    def printer(self):
        text = ""        
        text += "Score: {}".format(len(self.snake.body)*5)

        for row in range(self.height):
            text += "\n"
            for col in range(self.width):
                text += self.map[row][col].t
        os.system('clear')
        print (text)

def create_matrix(height,width):
    mat = []
    for row in range(height):
        mat.append([])
        for column in range(width):
            mat[row].append(space())
    return mat

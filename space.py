class space():
    def __init__(self, t = ' '):
        self.t = t
    def action(self,snake):
        pass
class unit(space):
    def __init__(self,t,y,x,game):
        space.__init__(self,t = t)
        self.game = game
        self.x = x
        self.y = y
        self.game.map[y][x] = self #declare place in matrix self 
    def replace(self,new_space):
        self.game.map[self.y][self.x] = new_space
    
stf = space()
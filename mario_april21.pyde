class Game:
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
    
    def display(self):
        line(0,self.g,self.w, self.g)
            
class Creature:
    def __init__(self,x,y,r,g):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
    
    def display(self):
        ellipse(self.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r, self.g,self.x+self.r,self.g)
        stroke(255)
        
class Mario(Creature):
    def __init__(self,x,y,r,g):
        Creature.__init__(self,x,y,r,g)


game = Game(800,600,500)
mario = Mario(50,400,10,game.g)



def setup():
    size(game.w, game.h)
    background(0)
    stroke(255)

def draw():
    background(0)
    game.display()
    mario.display()

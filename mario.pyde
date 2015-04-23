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
        self.vx=0
        self.vy=0
    
    def display(self):
        self.update()
        ellipse(self.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r, self.g,self.x+self.r,self.g)
        stroke(255)
        
class Mario(Creature):
    def __init__(self,x,y,r,g):
        Creature.__init__(self,x,y,r,g)
        self.Keys={UP:False,LEFT:False,RIGHT:False}
    
    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
            self.y+=self.vy
        else:
            self.vy=0




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
    
def keyPressed():
    mario.Keys[keyCode]=True

def keyReleased():
    mario.Keys[keyCode]=False
    

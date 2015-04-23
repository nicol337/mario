class Game:
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
    
    def display(self):
        line(0,self.g,self.w, self.g)
            
class Creature:
    def __init__(self,x,y,r,g,rImg,rF):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.rImg=loadImage(rImg)
        self.f=0
        self.rF=rF
        
    def display(self):
        self.update()
#         ellipse(self.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r, self.g,self.x+self.r,self.g)
        stroke(255)
        self.f=(self.f+0.1)%self.rF
        if self.vx>0:
            image(self.rImg,self.x-self.r,self.y-self.r,60,78,int(self.f)*60,0,int(self.f)*60+60,78)
        elif self.vx<0:
            image(self.rImg,self.x-self.r,self.y-self.r,60,78,int(self.f)*60+60,0,int(self.f)*60,78)
class Mario(Creature):
    def __init__(self,x,y,r,g,rImg,rF):
        Creature.__init__(self,x,y,r,g,rImg,rF)
        self.Keys={UP:False,LEFT:False,RIGHT:False}
        self.img=loadImage(rImg)
    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r
        
        if self.Keys[UP] and self.vy == 0:
            self.vy=-5
            self.y+=self.vy
        
        elif self.Keys[LEFT]:
            self.vx=-1
        elif self.Keys[RIGHT]:
            self.vx=1
        else:
            self.vx=0

        self.x += self.vx
        
game = Game(800,600,500)
mario = Mario(50,100,39,game.g,'images/marioRun.png',4)

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
    

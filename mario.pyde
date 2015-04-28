class Game:
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.platforms=[]
        self.x = 0
        self.y = 0
        
        self.makePlatforms()
  
    def makePlatforms(self):
        for i,j in zip([100,200,300],[400,300,200]):
            self.platforms.append(Platform(i,j,100,20))
#             self.platforms.append(Platform(200,300,100,20))
#             self.platforms.append(Platform(300,200,100,20))
    
    def display(self):
        line(0,self.g,self.w, self.g)
        for p in self.platforms:
            p.display()

class Platform:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def display(self):
        rect(self.x-game.x,self.y-game.y, self.w, self.h)
                    
class Creature:
    def __init__(self,x,y,r,g,sImg,rImg,rF):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.rImg=loadImage(rImg)
        self.sImg=loadImage(sImg)
        self.f=0
        self.rF=rF
        self.dir=1
        
    def display(self):
        self.update()
#         ellipse(self.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r-game.x, self.g-game.y,self.x+self.r-game.x,self.g-game.y)
        stroke(255)
        self.f=(self.f+0.1)%self.rF
        if self.vx>0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,60,78,int(self.f)*60,0,int(self.f)*60+60,78)
        elif self.vx<0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,60,78,int(self.f)*60+60,0,int(self.f)*60,78)
        else:
            if self.dir>0:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y)
            else:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,60,78,60,0,0,78)
class Mario(Creature):
    def __init__(self,x,y,r,g,sImg,rImg,rF):
        Creature.__init__(self,x,y,r,g,sImg,rImg,rF)
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
            self.dir=-1
            
        elif self.Keys[RIGHT]:
            self.vx=1
            self.dir=1
        else:
            self.vx=0


        self.x += self.vx
        
        for p in game.platforms:
            if (self.y+self.r < p.y or self.g == p.y) and self.x in range(p.x,p.x+p.w+1):
                self.g = p.y 
                return True
        self.g=game.g
        
        if self.x - game.x >= game.w/2:
            game.x+=1
        elif game.x > 0:
            game.x -=1
game = Game(800,600,500)
mario = Mario(50,100,39,game.g,'images/marioStand.png','images/marioRun.png',4)

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
    

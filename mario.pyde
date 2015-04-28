class Game:
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.gImg = loadImage('images/platform2.png')
        self.platforms=[]
        self.enemies=[]
        self.x = 0
        self.y = 0
        
        self.makePlatforms()
        self.makeEnemies()
  
    def makePlatforms(self):
        for i,j in zip([100,100,200,300,1000],[300,400,300,200,400]):
            self.platforms.append(Platform(i,j,100,20))
#             self.platforms.append(Platform(200,300,100,20))
#             self.platforms.append(Platform(300,200,100,20))
    def makeEnemies(self):
        self.enemies.append(Tazmanian(500,300,700,self.g-19,39,self.g,'images/tazmanian.png','images/tazmanian.png',6,63,61))
        self.enemies.append(Tazmanian(100,100,200,self.g-19-100,39,self.g,'images/tazmanian.png','images/tazmanian.png',6,63,61))
        
    def display(self):
        line(0,self.g,self.w, self.g)
        image(self.gImg,0,self.g)
        image(self.gImg,0,self.g+50)
        for e in self.enemies:
            e.update()
            e.display()
        for p in self.platforms:
            p.display()

class Platform:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.gImg = loadImage('images/platform2.png')
    
    def display(self):
#         rect(self.x-game.x,self.y-game.y, self.w, self.h)
          image(self.gImg,self.x-game.x, self.y-game.y, self.w, self.h,0,0, self.w, self.h) 
                    
class Creature:
    def __init__(self,x,y,r,g,sImg,rImg,rF,w,h):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.w=w
        self.h=h
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
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w,0,int(self.f)*self.w+self.w,self.h)
        elif self.vx<0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w+self.w,0,int(self.f)*self.w,self.h)
        else:
            if self.dir>0:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y)
            else:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,self.w,0,0,self.h)
class Mario(Creature):
    def __init__(self,x,y,r,g,sImg,rImg,rF,w,h):
        Creature.__init__(self,x,y,r,g,sImg,rImg,rF,w,h)
        self.Keys={UP:False,LEFT:False,RIGHT:False}
        self.img=loadImage(rImg)

    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.2
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r
        
        if self.Keys[UP] and self.vy == 0:
            self.vy=-7
            self.y+=self.vy
        
        elif self.Keys[LEFT]:
            self.vx=-2
            self.dir=-1
            
        elif self.Keys[RIGHT]:
            self.vx=2
            self.dir=1
        else:
            self.vx=0


        self.x += self.vx
        
        if self.x - self.r <= 0:
            self.x = self.r
        
        if self.x - game.x >= game.w/2:
            game.x+=2
        elif game.x > 0 and self.vx!=0:
            game.x -=2
            
        for e,i in zip(game.enemies,range(len(game.enemies))):
            if self.distance(e) <= self.r+e.r:
                if self.vy > 0:
                    del game.enemies[i]
                else:
                    print("mario dead")
        
        for p in game.platforms:
            if (self.y+self.r < p.y or self.g == p.y) and self.x in range(p.x,p.x+p.w+1):
                self.g = p.y 
                return True
        self.g=game.g
        
    def distance(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
#         if self.x - game.x >= game.w/2:
#             game.x+=1
#         elif game.x > 0 and self.vx!=0:
#             game.x -=1
        
        
        
class Tazmanian(Creature):
    def __init__(self,x,x1,x2,y,r,g,sImg,rImg,rF,w,h):
        Creature.__init__(self,x,y,r,g,sImg,rImg,rF,w,h)
        self.x1=x1
        self.x2=x2
        self.vx=-1
        
    def update(self):
        if self.x<self.x1:
            self.vx = 1
        elif self.x>self.x2:
            self.vx=-1
        self.x+=self.vx
            
    
game = Game(800,600,500)
mario = Mario(50,100,39,game.g,'images/marioStand.png','images/marioRun.png',4,60,78)

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
    

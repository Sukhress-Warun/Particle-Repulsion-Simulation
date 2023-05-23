import sys
import pygame,os
from pygame.locals import *
import random

class object():
	def __init__(self,p,s,xv,yv,c):
		self.x=p[0]
		self.y=p[1]
		self.s=s
		self.c=c
		self.xv=xv
		self.yv=yv
		self.dislist=[]
	def speed(self):
		self.x+=self.xv
		self.y+=self.yv
		temp=inframe(self)
		if not temp[0]:
			if temp[1]=='x':
				self.x-=self.xv
				self.xv*=-1
				self.x+=self.xv
			else:
				self.y-=self.yv
				self.yv*=-1
				self.y+=self.yv
	def clamp(self,i):
				x,y,c=0,0,0
				# self.xv+=(w/2-self.x)*0.001
				# self.yv+=(h/2-self.y)*0.001
				for j in range(len(objl)):
					if(j!=i):
						if dis(self.x,self.y,objl[j].x,objl[j].y):
							x+=objl[j].x
							y+=objl[j].y
							c+=1
							self.dislist.append((objl[j].x,objl[j].y))
				if(self.x<=space):
					x+=0
					y+=self.y
					c+=1
					self.dislist.append((0,self.y))
				if(self.x>=w-space):
					x+=w
					y+=self.y
					c+=1
					self.dislist.append((w,self.y))
				if(self.y>=h-space):
					x+=self.x
					y+=h
					c+=1
					self.dislist.append((self.x,h))
				if(self.y<=space):
					x+=self.x
					y+=0
					c+=1
					self.dislist.append((self.x,0))
				if(c!=0):
					x/=c
					y/=c
					dx = x- objl[i].x
					dy = y- objl[i].y
					dx*=0.01
					dy*=0.01
					self.xv-=dx
					self.yv-=dy
				self.speed()
	def display(self):
		pygame.draw.circle(surface,tuple(self.c),(self.x,self.y),self.s)
		for i in self.dislist:
			pygame.draw.line(surface,tuple(self.c),i,(self.x,self.y),2)
		self.dislist=[]

def r(n,s=0):
	return random.randrange(s,n)

def ro(n):
	v=10
	for i in range(n):
		obj=object((r(w-space,space),r(h-space,space)),12,r(v,-v),r(v,-v),(r(255,100),r(255,100),r(255,100)))
		objl.append(obj)

def dis(x,y,x1,y1):
	d=(((x-x1)**2) + ((y-y1)**2))**0.5
	if d<=space:
		return True
	else:
		return False

def inframe(self):
	if(self.x-self.s<0 or self.x+self.s>w):
		return False,"x"
	elif (self.y-self.s<0 or self.y+self.s>h):
		return False,"y"
	else:
		return True,None

def tt(txt,s,c,p):
	font = pygame.font.Font('freesansbold.ttf',s)
	text = font.render(txt,True,c)
	textRect = text.get_rect()
	textRect.center = (p[0],p[1])
	surface.blit(text, textRect)


os.environ['SDL_VIDEO_CENTERED'] = '1' 
pygame.init()
info = pygame.display.Info()
w,h= info.current_w-100,info.current_h-100
surface = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()


space=50
particleNum=100
objl=[]
nexfram=[]
ro(particleNum)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	for i in range(len(objl)):
		objl[i].clamp(i)
		
	objl=list(filter(lambda ob:inframe(ob)[0],objl))

	surface.fill((0,0,0))

	for i in range(len(objl)):
		objl[i].display()
	
	tt(f"{len(objl)}",15,(0,255,0),(15,10))
	pygame.display.update()
	clock.tick(60)
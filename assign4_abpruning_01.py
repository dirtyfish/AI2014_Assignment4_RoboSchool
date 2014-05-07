#assign4_abpruning_01.py
import pygame, os, random, math
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]

print "Running in directory:",main_dir

black = (0,0,33) 
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,123,123) 

upcli="c:/windows/fonts/upcli.ttf"   ##seems to work for me
fontsize=44

#-2=very agressive
#-1=equal(zero sum)
#0=indifferent
#1=cooperation
#2=selfsacrifice

scrw=800
scrh=600
upcli="c:/windows/fonts/upcli.ttf"   ##seems to work for me
fontsize=15

agressionlevel=-1
nodes=[]

def randommovescore():
	return random.randint(0,255),random.randint(0,255)

for x in range(31):
	y=x
	level=0
	while y>>1>0:
		level+=1
		y>>=1
	tmp=list(randommovescore())
	if x==0:
		print 0
		tmp=[0,0]
	nodes.append([tmp,tmp[0]+tmp[1]*agressionlevel,level])

print nodes[1:16]

for x in range(31):
  nodes[x][1]+=nodes[x>>1][1]    



print nodes[1:16]







def main():
	if 1:
		#print list(randommovescore())
		pygame.init()
		mainClock = pygame.time.Clock()
		screen = pygame.display.set_mode((scrw, scrh), HWSURFACE|DOUBLEBUF)
		font=pygame.font.Font(upcli,fontsize)

		while 1:
		  screen.fill((200,133,100))
		  text= font.render("0", True, blue)
		  screen.blit(text, [scrw/2,scrh/2])


		  for e in pygame.event.get():
			   if e.type == QUIT:
			   	 return
			   
		  pygame.display.flip()
		  mainClock.tick(40)

main()
pygame.quit()
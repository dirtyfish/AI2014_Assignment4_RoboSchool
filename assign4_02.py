#!/usr/bin/env python

import pygame, os, random, math
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]

black = (0,0,33) 
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,123,123) 
screenw=1024
screenh=768
#fieldw=1024/2-48
fieldw=7*64
#fieldh=768/2
fieldh=6*64
fieldr=1024/2+63
fieldd=768/2

print fieldw/64,fieldh/64
print fieldw,fieldh
#black=0x000000
#black=66

instructions= ['UP','LEFT','DOWN','RIGHT','TURN LEFT','TURN RIGHT']
imagenamel=['instruction_up_cropped_96.tga']
imagenamel.append('instruction_left_cropped_96.tga')
imagenamel.append('instruction_down_cropped_96.tga')
imagenamel.append('instruction_right_cropped_96.tga')
imagenamel.append('instruction_turnleft_cropped_96.tga')
imagenamel.append('instruction_turnright_cropped_96.tga')
imagenamel.append('sky.png')
imagenamel.append('floor.jpg')
imagenamelist=[]
bitmaplist=[]
avgcolorlist=[]

def randomcolor():

    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def main():
    shuffled=0
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF)

    if 1:
        for imagename in imagenamel:
    
          fullimagename= os.path.join(main_dir, 'IMAGES',imagename)
          bitmap = pygame.image.load(fullimagename)      
          imagenamelist.append(fullimagename)
          bitmaplist.append(bitmap)

    print imagenamelist
  
    #get the image and screen in the same format
    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    #prep some variables
    anim = 0.0

    #mainloop 
    stopevents = QUIT, KEYDOWN, MOUSEBUTTONDOWN
    frame=0
    

    while 1:
        frame+=1
        screen.fill(black)
        for e in pygame.event.get():
            if e.type in stopevents:
                return
        
        posx=0
        for bitmap in bitmaplist:
            posx+=96
            adposx=posx+frame*2
            adposx%=screenh+96
            adposx-=96
            screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))


        #pygame.draw.rect(screen, blue, [0,0,fieldw,fieldh], 2)
        #pygame.draw.rect(screen, blue, [0,0,64,64], 2)
        #pygame.draw.rect(screen, blue, [0,0,32,32], 2)
        pygame.draw.rect(screen, blue, [0,fieldd,fieldw,fieldh], frame%2*5+1)
        pygame.draw.rect(screen, blue, [fieldr,0,fieldw,fieldh], frame%2+1)
        pygame.draw.rect(screen, blue, [fieldr,fieldd,fieldw,fieldh], frame%2+1) 

        screen.blit(bitmaplist[7], (0, fieldd), (frame, 0, fieldw,fieldh)) 
        screen.blit(bitmaplist[7], (0, 0), (0, frame, fieldw,fieldh)) 
        screen.blit(bitmaplist[7], (fieldr, 0), (frame, frame, fieldw,fieldh)) 
        screen.blit(bitmaplist[7], (fieldr, fieldd), (frame, 100.0*math.sin(frame/100.0), fieldw,fieldh)) 

        screen.blit(bitmaplist[0], (0, fieldd), (-frame, 0, fieldw,fieldh)) 
        screen.blit(bitmaplist[4], (fieldr, fieldd), (-frame, -frame*0.5, fieldw,fieldh)) 
        screen.blit(bitmaplist[2], (0, 0), (-frame, -100.0*math.sin(frame/100.0), fieldw,fieldh)) 
    
        pygame.display.flip()
        mainClock.tick(51)

if __name__ == '__main__': main()
pygame.quit()
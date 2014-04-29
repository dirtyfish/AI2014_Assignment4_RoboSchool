#!/usr/bin/env python



import pygame, os, random
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]


black = (0,0,33) 
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,123,123) 
screenw=1024
screenh=768
fieldw=1024/2-48
fieldh=768/2-1
fieldr=1024/2+48
fieldd=768/2+1



instructions= ['UP','LEFT','DOWN','RIGHT','TURN LEFT','TURN RIGHT']
imagenamel=['instruction_up_cropped_96.tga']
imagenamel.append('instruction_left_cropped_96.tga')
imagenamel.append('instruction_down_cropped_96.tga')
imagenamel.append('instruction_right_cropped_96.tga')
imagenamel.append('instruction_turnleft_cropped_96.tga')
imagenamel.append('instruction_turnright_cropped_96.tga')
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
          #print fullimagename
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
        if shuffled==0:
            random.shuffle(bitmaplist)
            shuffled=1
        for bitmap in bitmaplist:
            posx+=96
            adposx=posx+frame*2
            adposx%=screenh+96
            adposx-=96
            screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))


        pygame.draw.rect(screen, blue, [0,0,fieldw,fieldh], 2)
        pygame.draw.rect(screen, blue, [0,fieldd,fieldw,fieldh], 2)
        pygame.draw.rect(screen, blue, [fieldr,0,fieldw,fieldh], 2)
        pygame.draw.rect(screen, blue, [fieldr,fieldd,screenw/2-48,screenh/2-1], 2)
               

            
    


        pygame.display.flip()
        mainClock.tick(30)



if __name__ == '__main__': main()
pygame.quit()
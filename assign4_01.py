#!/usr/bin/env python



import pygame, os, random
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]


black = (255,255,255) #almost white
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,0,255) 


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

    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600), HWSURFACE|DOUBLEBUF)

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
        for bitmap in bitmaplist:
            posx+=96
            screen.blit(bitmap, (posx, 0), (0, 0, 96,96))
               

            
    


        pygame.display.flip()
        mainClock.tick(30)



if __name__ == '__main__': main()
pygame.quit()
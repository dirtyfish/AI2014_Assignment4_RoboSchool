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

upcli="c:/windows/fonts/upcli.ttf"   ##seems to work for me
fontsize=44


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
imagenamel.append('instruction_turnright_cropped_96.tga')
imagenamel.append('rs_title_c_32.tga')

tilenamel=['white.jpg','bluegrey.jpg','pattern.jpg','start.jpg','goal.jpg']
tilelist=[]
imagenamelist=[]
bitmaplist=[]
avgcolorlist=[]

def randomcolor():

    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def main():
    room=4
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenw, screenh), HWSURFACE|DOUBLEBUF)

    if 1:
        for imagename in imagenamel:
    
          fullimagename= os.path.join(main_dir, 'IMAGES',imagename)
          bitmap = pygame.image.load(fullimagename)      
          imagenamelist.append(fullimagename)
          bitmaplist.append(bitmap)

        for imagename in tilenamel:
    
          fullimagename= os.path.join(main_dir, 'IMAGES',imagename)
          bitmap = pygame.image.load(fullimagename)      
          imagenamelist.append(fullimagename)
          tilelist.append(bitmap)

    print imagenamelist
    print bitmaplist[7].get_size()
  
    #get the image and screen in the same format
    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    #prep some variables
    anim = 0.0



   
    stopevent = QUIT
    print stopevent
    frame=0

    if 1:

    # set up music'background.mid'
            #pickUpSound = pygame.mixer.Sound('pickup.wav')
            pygame.mixer.music.load('Power tools.mp3')
            pygame.mixer.music.play(0, 0)
            #pygame.mixer.music.play(0, 0.5)
            
    
 #mainloop ##################################################################################
    while 1:
        frame+=1
        screen.fill(black)
       



        if room<2:
            posx=0
            for bitmap in bitmaplist:
                
                adposx=posx+frame*2
                adposx%=screenh+96
                adposx-=96
                screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))
                posx+=96

            for bitmap in tilelist:
                
                adposx=posx+frame*2
                adposx%=screenh+96
                adposx-=96
                screen.blit(bitmap, (screenw/2-48, adposx), (0, 0, 96,96))
                posx+=64


        #pygame.draw.rect(screen, blue, [0,0,fieldw,fieldh], 2)
        #pygame.draw.rect(screen, blue, [0,0,64,64], 2)
        #pygame.draw.rect(screen, blue, [0,0,32,32], 2)
        if room==0:
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
            if frame>40:
                pygame.mixer.music.play(0, 0)
                room=1

        if room==1:
            pygame.draw.rect(screen, blue, [0,fieldd,fieldw,fieldh], frame%2*5+1)
            pygame.draw.rect(screen, blue, [fieldr,0,fieldw,fieldh], frame%2+1)
            pygame.draw.rect(screen, blue, [fieldr,fieldd,fieldw,fieldh], frame%2+1) 
            if frame>80:
                room=2
                frame=200
                #pygame.mixer.music.load('Power tools.mp3')
                pygame.mixer.music.play(0,0)

        if room==2:
            screen.fill((100,133,100))
            #bitmaplist[8].set_colorkey((255,255,255),0)
            #bitmaplist[8].set_alpha(255)
            #screen.blit(bitmaplist[9], (200, 0), (0, 0, 999,999)) 

            font=pygame.font.Font(upcli,fontsize*2)
           

            text= font.render("ROBOT SCHOOL", True, blue)
            screen.blit(text, [320,150+50*math.sin((frame*2-2)*0.05)])


            font=pygame.font.Font(upcli,fontsize)
            
            text= font.render("AI ASSIGNMENT 04", True, blue)
            screen.blit(text, [420,150+50*math.sin((frame-2)*0.05)])

            font=pygame.font.Font(upcli,fontsize*2/3)
            
            text= font.render("PRESS SPACE", True, blue)
            screen.blit(text, [466,350+50*math.sin((frame*2/3-2)*0.05)])

            text= font.render("PRESS I FOR INSTRUCTION", True, blue)
            screen.blit(text, [400,450+50*math.sin((frame*2/4-2)*0.05)])

            




            for e in pygame.event.get():
              if e.type == KEYDOWN:
                if e.key == ord(' '):
                  room=3
                  frame=500
                  pygame.mixer.music.fadeout(2999)
                if e.key == ord('i'):
                  room=4

                  #pygame.mixer.music.load('Power tools.mp3')
                  pygame.mixer.music.play(0, 0.5)
              if e.type == stopevent:
                return

        if room==4:
            screen.fill((100,133,100))
            #bitmaplist[8].set_colorkey((255,255,255),0)
            #bitmaplist[8].set_alpha(255)
            #screen.blit(bitmaplist[9], (200, 0), (0, 0, 999,999)) 

            font=pygame.font.Font(upcli,fontsize*2)
           

            text= font.render("INSTRUCTIONS", True, blue)
            screen.blit(text, [320,150+50*math.sin((frame*2-2)*0.05)])


            font=pygame.font.Font(upcli,fontsize)
            
            #text= font.render("AI ASSIGNMENT 04", True, blue)
            #screen.blit(text, [420,150+50*math.sin((frame-2)*0.05)])

            font=pygame.font.Font(upcli,fontsize*2/3)
            
            text= font.render("PRESS SPACE", True, blue)
            screen.blit(text, [466,350+50*math.sin((frame*2/3-2)*0.05)])

            text= font.render("YOU WILL CONTROL TWO ROBOTS", True, blue)
            screen.blit(text, [400,450+50*math.sin((frame*2/4-2)*0.05)])

            text= font.render("A - LEFT, D - RIGHT", True, blue)
            screen.blit(text, [400,550+50*math.sin((frame*2/4-2)*0.05)])

            




            for e in pygame.event.get():
              if e.type == KEYDOWN:
                if e.key == ord(' '):
                  room=3
                  frame=500
                  pygame.mixer.music.fadeout(2999)
                if e.key == ord('2'):
                  room=3
                  frame=500
                  #pygame.mixer.music.load('Power tools.mp3')
                  pygame.mixer.music.play(0, 0.5)
              if e.type == stopevent:
                return

        if room==3:
            screen.fill((00,133,100))
            if frame<600:
            
              font=pygame.font.Font(upcli,fontsize*2)
              text= font.render("START", True, black)
              screen.blit(text, [420,150+50*math.sin((frame*2-2)*0.05)])

            else:
                room=5
                frame=0

            
            
            #pygame.mixer.music.stop()
            #pygame.mixer.pause()

            for e in pygame.event.get():
              
              if e.type == stopevent:
                return


        if room==5:
            if frame==0:
                selcarddir=0
                cardlist=[]
                carddir=[]
                cards=10
                cardsleft=cards
                totdir=0
                for x in range(cards):
                    cardlist.append(random.randint(1,6))
                    carddir.append(0)




                print "cardlist:",cardlist

            screen.fill((55,133,33))
            screen.blit(bitmaplist[7], (0, fieldd), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (0, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (fieldr, 0), (0, 0, fieldw,fieldh)) 
            screen.blit(bitmaplist[7], (fieldr, fieldd), (0, 0, fieldw,fieldh)) 

            #screen.blit(bitmaplist[0], (0, fieldd), (-frame, 0, fieldw,fieldh)) 
            #screen.blit(bitmaplist[4], (fieldr, fieldd), (-frame, -frame*0.5, fieldw,fieldh)) 
            #screen.blit(bitmaplist[2], (0, 0), (-frame, -100.0*math.sin(frame/100.0), fieldw,fieldh))

            posx=0
            adposy=0
            
            nrcard=cards
            for card in cardlist:

                nrcard-=1
                bitmap=bitmaplist[card-1]
                adposx=posx+frame*1-200
                #adposx%=screenh+96
                adposx-=96

                if adposx==672:#decide direction
                    if totdir==cardsleft:
                        selcarddir=-1
                    if totdir==-cardsleft:
                        selcarddir=1

                    if selcarddir==0:
                      selcarddir=nrcard%2*2-1

                    carddir[nrcard]=selcarddir
                    cardsleft-=1
                    totdir+=selcarddir


                if adposx>672:#card changes direction
                   
                    adposy=adposx-672
                    adposx=672


                screen.blit(bitmap, (screenw/2-48+adposy*(carddir[nrcard]), adposx), (0, 0, 96,96))
                font=pygame.font.Font(upcli,fontsize*2/3)
                text= font.render(str(nrcard), True, (255,255,255))
                #text= font.render(str(totdir), True, (255,255,255))
                screen.blit(text, [screenw/2-48+adposy*(carddir[nrcard])+5, adposx+5])
                #if frame>=48:
                 #   frame=48

                posx+=96




            for e in pygame.event.get():
              if e.type == KEYDOWN:
                if e.key == ord('a'):
                  selcarddir=-1
                if e.key == ord('d'):  
                  selcarddir=1
                  
              
              if e.type == stopevent:
                return




        
        pygame.display.flip()
        mainClock.tick(40)

if __name__ == '__main__': main()
pygame.quit()
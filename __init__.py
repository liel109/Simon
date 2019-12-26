import pygame
import os
import random

def Write(msg="pygame is cool"):
        myfont = pygame.font.SysFont("None", 40)
        mytext = myfont.render(msg, True, (255,0,0))
        mytext = mytext.convert_alpha()
        return mytext
        
def DidTouch(posx,posy):
    if(posx>redx and posx<redx+red.get_width() and posy>redy and posy<redy+red.get_height()):
        if(screen.get_at((posx,posy))==redcolor):
            return 0
    elif(posx>bluex and posx<bluex+blue.get_width() and posy>bluey and posy<bluey+blue.get_height()):
        if(screen.get_at((posx,posy))==bluecolor):
            return 1
    elif(posx>yellowx and posx<yellowx+yellow.get_width() and posy>yellowy and posy<yellowy+yellow.get_height()):
        if(screen.get_at((posx,posy))==yellowcolor):
            return 2
    elif(posx>greenx and posx<greenx+green.get_width() and posy>greeny and posy<greeny+green.get_height()):
        if(screen.get_at((posx,posy))==greencolor):
            return 3
    else: return 4

def Glowin(pressed):
    seconds=0
    milseconds=0
    delta=0.3
    if(pressed==0):
        w=red.get_width()
        h=red.get_height()
        x=redx
        y=redy
        while (seconds<=2):
            milseconds = clock.tick(FPS)
            seconds += milseconds/1000
            pygame.display.set_caption(str(seconds))
            if(seconds<=1):
                w += delta*seconds
                h += delta*seconds
                x -= delta*seconds/2
                y -= delta*seconds/2
                copy=pygame.transform.scale(red,(round(w),round(h)))
                screen.blit(background,(0,0))
                screen.blit(yellow,(yellowx,yellowy))
                screen.blit(blue,(bluex,bluey))
                screen.blit(green,(greenx,greeny))
                screen.blit(copy,(x,y))
                pygame.display.flip()
            else:
                if(w>=150 or h>=150):
                    w -= delta*seconds
                    h -= delta*seconds
                    x += delta*seconds/2
                    y += delta*seconds/2
                    copy=pygame.transform.scale(red,(round(w),round(h)))
                    screen.blit(background,(0,0))
                    screen.blit(yellow,(yellowx,yellowy))
                    screen.blit(blue,(bluex,bluey))
                    screen.blit(green,(greenx,greeny))
                    screen.blit(copy,(x,y))
                    pygame.display.flip()
                    
    if(pressed==1):
        w=blue.get_width()
        h=blue.get_height()
        x=bluex
        y=bluey
        while (seconds<=2):
            milseconds = clock.tick(FPS)
            seconds += milseconds/1000
            pygame.display.set_caption(str(seconds))
            if(seconds<=1):
                w += delta*seconds
                h += delta*seconds
                x -= delta*seconds/2
                y -= delta*seconds/2
                copy=pygame.transform.scale(blue,(round(w),round(h)))
                screen.blit(background,(0,0))
                screen.blit(yellow,(yellowx,yellowy))
                screen.blit(red,(redx,redy))
                screen.blit(green,(greenx,greeny))
                screen.blit(copy,(x,y))
                pygame.display.flip()
            else:
                if(w>=150 or h>=150):
                    w -= delta*seconds
                    h -= delta*seconds
                    x += delta*seconds/2
                    y += delta*seconds/2
                    copy=pygame.transform.scale(blue,(round(w),round(h)))
                    screen.blit(background,(0,0))
                    screen.blit(yellow,(yellowx,yellowy))
                    screen.blit(red,(redx,redy))
                    screen.blit(green,(greenx,greeny))
                    screen.blit(copy,(x,y))
                    pygame.display.flip()
                    
    if(pressed==2):
        w=yellow.get_width()
        h=yellow.get_height()
        x=yellowx
        y=yellowy
        while (seconds<=2):
            milseconds = clock.tick(FPS)
            seconds += milseconds/1000
            pygame.display.set_caption(str(seconds))
            if(seconds<=1):
                w += delta*seconds
                h += delta*seconds
                x -= delta*seconds/2
                y -= delta*seconds/2
                copy=pygame.transform.scale(yellow,(round(w),round(h)))
                screen.blit(background,(0,0))
                screen.blit(blue,(bluex,bluey))
                screen.blit(red,(redx,redy))
                screen.blit(green,(greenx,greeny))
                screen.blit(copy,(x,y))
                pygame.display.flip()
            else:
                if(w>=150 or h>=150):
                    w -= delta*seconds
                    h -= delta*seconds
                    x += delta*seconds/2
                    y += delta*seconds/2
                    copy=pygame.transform.scale(yellow,(round(w),round(h)))
                    screen.blit(background,(0,0))
                    screen.blit(blue,(bluex,bluey))
                    screen.blit(red,(redx,redy))
                    screen.blit(green,(greenx,greeny))
                    screen.blit(copy,(x,y))
                    pygame.display.flip()
                    
    if(pressed==3):
        w=green.get_width()
        h=green.get_height()
        x=greenx
        y=greeny
        while (seconds<=2):
            milseconds = clock.tick(FPS)
            seconds += milseconds/1000
            pygame.display.set_caption(str(seconds))
            if(seconds<=1):
                w += delta*seconds
                h += delta*seconds
                x -= delta*seconds/2
                y -= delta*seconds/2
                copy=pygame.transform.scale(green,(round(w),round(h)))
                screen.blit(background,(0,0))
                screen.blit(blue,(bluex,bluey))
                screen.blit(red,(redx,redy))
                screen.blit(yellow,(yellowx,yellowy))
                screen.blit(copy,(x,y))
                pygame.display.flip()
            else:
                if(w>=150 or h>=150):
                    w -= delta*seconds
                    h -= delta*seconds
                    x += delta*seconds/2
                    y += delta*seconds/2
                    copy=pygame.transform.scale(green,(round(w),round(h)))
                    screen.blit(background,(0,0))
                    screen.blit(blue,(bluex,bluey))
                    screen.blit(red,(redx,redy))
                    screen.blit(yellow,(yellowx,yellowy))
                    screen.blit(copy,(x,y))
                    pygame.display.flip()


                
def SimonTurn():
    sounds.append(random.randint(0,3))
    for sound in sounds:
        if(sound==0):
            cnote.play()
                         
        if(sound==1):
            dnote.play()
            
        if(sound==2):
            enote.play()
                         
        if(sound==3):
            fnote.play()
            
        Glowin(sound)
                        
                   
    return

def TapCheck(turn,pressed):
    if(pressed==sounds[turn-1]): return True
    else: return False
        
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((640,400))
try:
    background=pygame.image.load(os.path.join("data","wood.jpg"))
    center=pygame.image.load(os.path.join("data","center.png"))
    blue=pygame.image.load(os.path.join("data","blue.png"))
    yellow=pygame.image.load(os.path.join("data","yellow.png"))
    red=pygame.image.load(os.path.join("data","red.png"))
    green=pygame.image.load(os.path.join("data","green.png"))
    cnote=pygame.mixer.Sound(os.path.join('data','c-note.wav'))
    enote=pygame.mixer.Sound(os.path.join('data','e-note.wav'))
    fnote=pygame.mixer.Sound(os.path.join('data','f-note.wav'))
    dnote=pygame.mixer.Sound(os.path.join('data','d-note.wav'))
except:
    raise UserWarning("Couldn't load files")

#rescale
background=pygame.transform.scale(background,(screen.get_width(),screen.get_height()))
center=pygame.transform.scale(center,(150,150))
blue=pygame.transform.scale(blue,(150,150))
yellow=pygame.transform.scale(yellow,(150,150))
red=pygame.transform.scale(red,(150,150))
green=pygame.transform.scale(green,(150,150))
center=pygame.transform.scale(center,(150,150))

#preparing the images
center.set_colorkey((255,255,255))
blue.set_colorkey((255,255,255))
yellow.set_colorkey((255,255,255))
red.set_colorkey((255,255,255))
green.set_colorkey((255,255,255))

background= background.convert()
center= center.convert_alpha()
blue= blue.convert_alpha()
yellow= yellow.convert_alpha()
red= red.convert_alpha()
green= green.convert_alpha()

#saving colors
redcolor=red.get_at((int(red.get_width()/2),int(red.get_height()/2)))
bluecolor=blue.get_at((int(blue.get_width()/2),int(blue.get_height()/2)))
yellowcolor=yellow.get_at((int(yellow.get_width()/2),int(yellow.get_height()/2)))
greencolor=green.get_at((int(green.get_width()/2),int(green.get_height()/2)))

#positions
redx=(screen.get_width()/2)-(red.get_width()/2)-75
redy=(screen.get_height()/2)-(red.get_height()/2)-75

yellowx=(screen.get_width()/2)-(yellow.get_width()/2)+75
yellowy=(screen.get_height()/2)-(yellow.get_height()/2)-75

bluex=(screen.get_width()/2)-(blue.get_width()/2)-75
bluey=(screen.get_height()/2)-(blue.get_height()/2)+75

greenx=(screen.get_width()/2)-(green.get_width()/2)+75
greeny=(screen.get_height()/2)-(green.get_height()/2)+75

#blitting
background.blit(center,((screen.get_width()/2)-(center.get_width()/2),(screen.get_height()/2)-(center.get_height()/2)))
screen.blit(background,(0,0))
screen.blit(red,(redx,redy))
screen.blit(yellow,(yellowx,yellowy))
screen.blit(blue,(bluex,bluey))
screen.blit(green,(greenx,greeny))

pygame.display.flip()

#defining
sounds=[]
mainloop=True
FPS=100
clock=pygame.time.Clock()
turn=0
tapped=[]
SimonTurn()
while mainloop:
    milliseconds = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            pressed=DidTouch(x,y)
            tapped.append(pressed)
            
            if(pressed==0):
                cnote.play()
                Glowin(pressed)
                turn+=1
                if TapCheck(turn,pressed):
                    if(turn==len(sounds)):
                        turn=0
                        SimonTurn()
                else:
                    finish=Write("Game Over!")
                    screen.blit(finish,(screen.get_width()/2-finish.get_width()/2,screen.get_height()/2-finish.get_height()/2))
                    pygame.display.flip()
                    break
                
                
            elif(pressed==1):
                dnote.play()
                Glowin(pressed)
                turn+=1
                if TapCheck(turn,pressed):
                    if(turn==len(sounds)):
                        turn=0
                        SimonTurn()
                else:
                    finish=Write("Game Over!")
                    screen.blit(finish,(screen.get_width()/2-finish.get_width()/2,screen.get_height()/2-finish.get_height()/2))
                    pygame.display.flip()
                    break
                
            elif(pressed==2):
                enote.play()
                Glowin(pressed)
                turn+=1
                if TapCheck(turn,pressed):
                    if(turn==len(sounds)):
                        turn=0
                        SimonTurn()
                else:
                    finish=Write("Game Over!")
                    screen.blit(finish,(screen.get_width()/2-finish.get_width()/2,screen.get_height()/2-finish.get_height()/2))
                    pygame.display.flip()
                    break
                
            elif(pressed==3):
                fnote.play()
                Glowin(pressed)
                turn+=1
                if TapCheck(turn,pressed):
                    if(turn==len(sounds)):
                        turn=0
                        SimonTurn()
                else:
                    finish=Write("Game Over!")
                    screen.blit(finish,(screen.get_width()/2-finish.get_width()/2,screen.get_height()/2-finish.get_height()/2))
                    pygame.display.flip()
                    break
                
            else: print("nothing")
            
            
            
        


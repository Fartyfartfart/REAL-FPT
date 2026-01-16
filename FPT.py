'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet) FPT
Program Description: FPT

-----------------------------------------------------------------------------
References: N/A

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:
 n?A
(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''



# *********SETUP**********
import pygame
import random
#Initalize pygame
pygame.init()
#WINDOW SETUP
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption ("Pygame FPT Niinja Frog Jump MiniGame")
clock = pygame.time.Clock ()
running = True
MENU = "menu"
GAME = "game"
GAME_OVER = "gameover"
game_state = MENU
#The font
font = pygame.font.Font ("minecraft.ttf", 32)
title_font = pygame.font.Font ("minecraft.ttf", 48)
#SCORE
score = 0
#LOAD OBJECT Image
Background = pygame.image.load ("nfbg.jpg")
Frog = pygame.image.load ("idle05.png")
size = random.randint (75,100)
Frog = pygame.transform.scale (Frog, (size,size))
Frog_x = random.randint (0, SCREEN_WIDTH - size)
Frog_y = random.randint (0, SCREEN_HEIGHT - size)
object_rect = Frog.get_rect (topleft= (Frog_x, Frog_y))
object1 = pygame.image.load ("")
object2 = pygame.image.load ("")
object_images = [object1,object2]

#Sound
click_sound = pygame.mixer.Sound ("strangerThings.mp3")

while running:
    screen.fill (0,0,0) #background
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False

        #Start game on click
        if game_state == MENU and event.type == pygame.MOUSEBUTTONDOWN:
           game_state = GAME
        if game_state == GAME and event.type == pygame.MOUSEBUTTONDOWN:
            if object_rect.collidepoint(pygame.mouse.get_pos()):
                score +=1
                click_sound.play ()
                #RESPAWN OBJECT
                size = random.randint (75,100)
                Frog = pygame.transform.scale (random.choice(Frog),(size,size))
                Frog_x = random.randint (0, SCREEN_WIDTH - size)
                Frog_y = random.randint (0, SCREEN_HEIGHT - size)
                object_rect = Frog.get_rect (topleft= (Frog_x, Frog_y))
        if game_state == MENU:
            title_text = title_font.render ("CLICK OBJECT", True, (255,255,255))
            start_text = font.render ("click to start", True, (255,255,255))
            screen.blit (title_text, (120,120))
            screen.blit (start_text, (200,200))

        elif game_state == GAME:
            screen.blit (Frog, object_rect)
            score_text = font.render (f"Score: {score}", True, (255,255,255))
            screen.blit (start_text, (10,10))
            if score >= 15:
                game_state = GAME_OVER

        #GAME OVER
        elif game_state == GAME_OVER:
            over_text = title_font.render ("Game OVER", True (255,0,0))
            final_Score = font.render (f"Score: {score}", True, (255,255,255))
            screen.blit (over_text (150, 150))
            screen.blit (over_text (200, 220))
        pygame.display.flip ()
        

        
         
# *********GAME LOOP**********




    # *********EVENTS**********

   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********

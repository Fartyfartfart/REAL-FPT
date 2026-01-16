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

pygame.init()

# WINDOW SETUP
SCREEN_WIDTH = 600 #width and heigh of the screen
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Ninja Frog Jump MiniGame") #Name for the top left of the code
clock = pygame.time.Clock()
running = True

# GAME STATES
MENU = "menu"
GAME = "game"
GAME_OVER = "gameover"
game_state = MENU

# FONTS
font = pygame.font.Font("minecraft.ttf", 32) #Font is set up so you can use it later on
title_font = pygame.font.Font("minecraft.ttf", 48)

# SCORE
score = 0

Saw = pygame.image.load("saw05.png") #Variable for the images needed for the game
Background = pygame.image.load("nfbg.jpg")
object1 = pygame.image.load("idle05.png")
object2 = pygame.image.load("jump.png")
object_images = [object1, object2]
TITLENINJAFROG = pygame.image.load("title.png")
Instructions = pygame.image.load("instructions.png")


size = random.randint(96, 96)
size1 = random.randint(32, 50)
Frog = pygame.transform.scale(random.choice(object_images), (size, size))
Saw = pygame.transform.scale(random.choice(object_images), (size1, size1))
Frog_x = random.randint(0, SCREEN_WIDTH - size)
Frog_y = random.randint(0, SCREEN_HEIGHT - size)
Frog_rect = Frog.get_rect(topleft=(Frog_x, Frog_y))

# SOUND
click_sound = pygame.mixer.Sound("strangerThings.mp3") # displays the music and keeps it in mind

while running:
    screen.blit(Background, (0, 0))
    screen.blit(TITLENINJAFROG, (30, 30))
    screen.blit(Instructions, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == MENU and event.type == pygame.MOUSEBUTTONDOWN: #if the mouse is pressed down takes you to the game and score is set to 0
            game_state = GAME
            score = 0

        if game_state == GAME and event.type == pygame.MOUSEBUTTONDOWN:
            if Frog_rect.collidepoint(pygame.mouse.get_pos()):
                score += 1
                click_sound.play()

                size = random.randint(75, 100)
                Frog = pygame.transform.scale(
                    random.choice(object_images), (size, size)
                )
                Frog_x = random.randint(0, SCREEN_WIDTH - size)
                Frog_y = random.randint(0, SCREEN_HEIGHT - size)
                Frog_rect = Frog.get_rect(topleft=(Frog_x, Frog_y))

    # MENU
    if game_state == MENU:
        title_text = title_font.render("CLICK OBJECT", True, (255, 255, 255))
        start_text = font.render("Click to start", True, (255, 255, 255))
        screen.blit(title_text, (150, 120))
        screen.blit(start_text, (200, 200))

    # GAME
    elif game_state == GAME:
        screen.blit(Frog, Frog_rect)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if score >= 15:
            game_state = GAME_OVER

    # GAME OVER
    elif game_state == GAME_OVER:
        over_text = title_font.render("GAME OVER", True, (255, 0, 0))
        final_score = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(over_text, (150, 140))
        screen.blit(final_score, (200, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

        
         
# *********GAME LOOP**********




    # *********EVENTS**********

   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********

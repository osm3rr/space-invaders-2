from nis import match
import pygame 
import random
# math library
import math
#library to reproduce the sounds
from pygame import mixer

# initializate pygame
pygame.init()

# windows size
screen_width = 800
screen_height = 600

# put the images in variables
bg_image = "night_space.png"
icon_image = "ufo.png"
player_image = "player.png"
alien_image = "alien33.png"
bullet_image = "tomato.png"

# size variable
size = ( screen_width, screen_height )

# show the window
screen = pygame.display.set_mode( size )

# background image
backgound = pygame.image.load( bg_image )

#background music
mixer.music.load( "gamemusic.wav" )
mixer.music.play( -1 )

# title
pygame.display.set_caption( "Space invaders @adakademy" )

# icon 
icon = pygame.image.load( icon_image )
pygame.display.set_icon( icon )

# player
player_img = pygame.image.load( player_image )
player_x = 370
player_y = 480
player_x_change = 0

# list of parameters for multiple enemies 
enemy_img = []
enemy_x = []
enemy_y = []
enemy_y_change = []
enemy_x_change = []

#  number of enemies
number_enemies = 8

# create a for loop for add the enemies 
for item in range( number_enemies ):
    enemy_img.append( pygame.image.load( alien_image ) )
    enemy_x.append( random.randint( 0, 735 ) )
    enemy_y.append( random.randint( 50, 150 ) )
    enemy_x_change.append( 4 )
    enemy_y_change.append( 40 )

# bullet definition
bullet_img = pygame.image.load( bullet_image )
bullet_x = 0
bullet_y = 480 # the same x coordinate of spaceship
bullet_x_change = 0
bullet_y_change = 20
bullet_state = "ready"

# score variable
score = 0

# font variable
score_font = pygame.font.Font( "stocky.ttf", 32 )

# text position in the scren
text_x = 10
text_y = 10

# |||||||| v16_4/6: game over font (line:85)
go_font = pygame.font.Font( "stocky.ttf", 64 )
go_x = 200
go_y = 250

# |||||||| v16_5/6: game over function (line:90)
def game_over( x,y ):
    go_text = go_font.render( "GAME OVER!!!", True, ( 255, 255, 255 ) )
    # |||||||| v16_6/6: show the text on the screen (line:93)
    screen.blit( go_text, ( x, y ) )

# function to show the text on the screen 
def show_text( x, y ):
    score_text = score_font.render( "SCORE: " + str( score ), True, ( 255, 255, 255 ) )
    # show the text on the screen
    screen.blit( score_text, ( x, y ) )

# player function
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# enemy function
def enemy(x, y, item):
    screen.blit( enemy_img[item], ( x, y ) )

# create fire function
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    # the initial position of the bullet
    screen.blit( bullet_img, ( x + 16, y + 10 ) )

# function to detect the collision
def is_collision( enemy_x, enemy_y, bullet_x, bullet_y ):
    distance = math.sqrt( ( enemy_x - bullet_x )**2 + ( enemy_y - bullet_y )**2 )
    
    if distance < 27: # this value is by trial and error
        return True
    else:
        return False

# Game loop
running = True
while running:
     
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed,
        # check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                # change the player speed
                player_x_change = -15 
                
            if event.key == pygame.K_RIGHT:
                # change the player speed
                player_x_change = 15
            
            # detect space key 
            if event.key == pygame.K_SPACE:
                # review the bullet state
                if bullet_state == "ready":
                    # bullet sound
                    bullet_sound = mixer.Sound( "shotgun.wav" )
                    bullet_sound.play()

                    # set bullet_x to player_x
                    bullet_x = player_x
                    # change player_x to bullet_x
                    fire( bullet_x, bullet_y )

        # review if keystroke was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # reset the rate change variable and remove the test print()
                player_x_change = 0
                    
    # RGB -> Red, Green, Blue 
    rgb = ( 0, 0, 0)
    screen.fill( rgb )

    # Show the background
    screen.blit( backgound, (0, 0) )
    
    # incremente or decrement the x variable 
    player_x += player_x_change
    
    # player x boundaries left
    if player_x <= 0:
        player_x = 0
        
    # this value 736, is according to 
    # the size of the player image
    # player boundaries right
    elif player_x >= 736: 
        player_x = 736

    #  create a for loop for add the enemies
    for item in range( number_enemies ):

        # |||||||| v16_1/6: Game over zone (line:188)
        if enemy_y[ item ] > 440:
            for j in range( number_enemies ):
                enemy_y[ j ] = 2000

                # |||||||| v16_2/6: Call game_over function (line:193)
            game_over( go_x, go_y )

            # |||||||| v16_3/6: break the loop (line:196)
            break

        enemy_x[item] += enemy_x_change[item]
        
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 6
            enemy_y[item] += enemy_y_change[item]
        
        elif enemy_x[item] >= 736: 
            enemy_x_change[item] = -6
            enemy_y[item] += enemy_y_change[item]
        
        # calculate the collision
        # and add the index to the enemy
        collision = is_collision( enemy_x[item], enemy_y[item], bullet_x, bullet_y )
        
        if collision:
            # explosion sound
            explosion_sound = mixer.Sound( "big-impact.wav" )
            explosion_sound.play()

            bullet_y = 480
            bullet_state = "ready"
            score += 1
            enemy_x[item] = random.randint( 0, 735 )
            enemy_y[item] = random.randint( 50, 150 )
        
        # calling to enemy function 
        enemy( enemy_x[item], enemy_y[item], item )

    # logic for bullet movement

    # logic for multiple bullet
    if bullet_y <= 0: # 0 is the condition for the bullet
        # reset the bullet position
        bullet_y = 480
        # reset the bullet state
        bullet_state = "ready"

    if bullet_state == "fire":
        # set fire function with bullet_x
        # instead player_x
        fire( bullet_x, bullet_y )
        # bullet movement
        bullet_y -= bullet_y_change

    # add the arguments to function
    player( player_x, player_y )
    
    # call show_text function
    show_text( text_x, text_y )

    # update the window 
    pygame.display.update()
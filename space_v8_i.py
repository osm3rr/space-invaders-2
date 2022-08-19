# pygame library
import pygame 
# random library
import random

# initializate pygame
pygame.init()

# windows size
screen_width = 800
screen_height = 600

# size variable
size = ( screen_width, screen_height )

# Display the windows
screen = pygame.display.set_mode( size )

# title
pygame.display.set_caption( "Space invaders @adakademy" )

# icon 
icon = pygame.image.load( "ufo.png" )
pygame.display.set_icon( icon )

# player definition
player_img = pygame.image.load( "player.png" )
player_x = 370
player_y = 480
# adding the rate change in x
player_x_change = 0

# enemy definition
enemy_img = pygame.image.load( "alien.png" )

# randoom movement of the enemy in x
# enemy_x = 370
enemy_x = random.randint( 0, 800 )

# randoom movement of the enemy in y
# enemy_y = 50
enemy_y = random.randint( 50, 150 )

# ||||||||| v8_1/5: change the value of rate change in "x"
enemy_x_change = 0.3

# ||||||||| v8_5/5: change the value of rate change in "y"
enemy_y_change = 40

# player function
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# enemy function
def enemy(x, y):
    screen.blit( enemy_img, ( x, y ) )

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
                # movement to left and remove the test print()
                player_x_change = -0.5
                
            if event.key == pygame.K_RIGHT:
                # movement to right and remove the test print()
                player_x_change = 0.5
                
            # review if keystroke was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # reset the rate change variable and remove the test print()
                player_x_change = 0
                #print( "keystroke was released" )
    
    # RGB -> Red, Green, Blue 
    rgb = ( 0, 0, 0)
    screen.fill( rgb )
    
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

    # |||||||| v8_2/5: logic for movement of the enemy
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.5
        # |||||||| v8_4/5: increment the value of the 
        # "y" coordinate of the enemy
        enemy_y += enemy_y_change

    #||||||| v8_3/5: size of the enemy is according 
    # to size of the enemy in px. in this case the enemy
    # size is 24 px, this is: 800 - 24: 776
      
    elif enemy_x >= 776: 
        enemy_x_change = -0.5
        # |||||||| v8_5/5: increment the value of the 
        # "y" coordinate of the enemy
        enemy_y += enemy_y_change
    
    # add the arguments to function
    player( player_x, player_y )

    # calling to enemy function
    enemy( enemy_x, enemy_y )
    
    # update the window 
    pygame.display.update()
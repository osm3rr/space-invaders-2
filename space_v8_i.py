# v1_1: pygame library
import pygame 
# v7_4/6: random library
import random

# v1_2: initializate pygame
pygame.init()

# v1_3: windows size
screen_width = 800
screen_height = 600

# v1_4: size variable
size = ( screen_width, screen_height )

# v1_5: Display the windows
screen = pygame.display.set_mode( size )

# v2_1: title
pygame.display.set_caption( "Space invaders @adakademy" )

# v2_2: icon 
icon = pygame.image.load( "ufo.png" )
pygame.display.set_icon( icon )

# v3_1: player
player_img = pygame.image.load( "player.png" )
player_x = 370
player_y = 480
# v5_4: add the rate change in x
player_x_change = 0

# v7_1/6: enemy definition
enemy_img = pygame.image.load( "alien.png" )

#v7_5/6: randoom movement of the enemy in x
# enemy_x = 370
enemy_x = random.randint( 0, 800 )

# v7_6/6: randoom movement of the enemy in y
# enemy_y = 50
enemy_y = random.randint( 50, 150 )

# ||||||||| v8_1/5: change the value of rate change in "x"
enemy_x_change = 0.3

# ||||||||| v8_5/5: change the value of rate change in "y"
enemy_y_change = 40

# v3_2: player function
# def player():
#     screen.blit( player_img, ( player_x, player_y ) )

# v4_1: add in the player function the parameter x and y
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# v7_2/6: enemy function
def enemy(x, y):
    screen.blit( enemy_img, ( x, y ) )

# v1_6: Game loop
running = True
while running:
    
    # v5_1: remove the variable player_y and the 
    # test print( player_y )     
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        # v5_2: if keystroke is pressed,
        # check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #V5_5: movement to left and remove the test print()
                player_x_change = -0.5
                
            if event.key == pygame.K_RIGHT:
                #V5_6: movement to right and remove the test print()
                player_x_change = 0.5
                
            #  v5_3: review if keystroke was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #V5_7: reset the rate change variable and remove the test print()
                player_x_change = 0
                #print( "keystroke was released" )
    
    # v2_3: RGB -> Red, Green, Blue 
    rgb = ( 0, 0, 0)
    screen.fill( rgb )
    
    # v5_8: incremente or decrement the x variable 
    player_x += player_x_change
    
    # v6_1/2: player x boundaries left
    if player_x <= 0:
        player_x = 0
        
    # v6_2/2: this value 736, is according to 
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
    
    # v4_2: add the arguments to function
    player( player_x, player_y )

    # v7_3/6: calling to enemy function
    enemy( enemy_x, enemy_y )
    
    # v2_4: update the window 
    pygame.display.update()
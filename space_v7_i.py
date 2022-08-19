# pygame library
import pygame 
# |||||||| v7_4/6: random library
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

# player
player_img = pygame.image.load( "player.png" )
player_x = 370
player_y = 480
# add the rate change in x
player_x_change = 0

#||||||| v7_1/6: load enemy image
enemy_img = pygame.image.load( "alien.png" )

# |||||||| v7_5/6: randoom movement of the enemy in x
# enemy_x = 370
enemy_x = random.randint( 0, 800 )

# |||||||| v7_6/6: randoom movement of the enemy in y
# enemy_y = 50
enemy_y = random.randint( 50, 150 )
enemy_x_change = 0

# player function
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# ||||||| v7_2/6: enemy function
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
                
            #  review if keystroke was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # reset the rate change variable and remove the test print()
                player_x_change = 0
    
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
    
    # add the arguments to function
    player( player_x, player_y )

    # ||||||| v7_3/6: enemy function call
    enemy( enemy_x, enemy_y )
    
    # update the window 
    pygame.display.update()
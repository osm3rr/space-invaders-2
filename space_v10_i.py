import pygame 
import random

# initializate pygame
pygame.init()

# windows size
screen_width = 800
screen_height = 600

# size variable
size = ( screen_width, screen_height )

# show the window
screen = pygame.display.set_mode( size )

# background image
backgound = pygame.image.load( "bg.png" )

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

# enemy definition
enemy_img = pygame.image.load( "alien.png" )

# randoom movement of the enemy in x
# enemy_x = 370
enemy_x = random.randint( 0, 800 )

# randoom movement of the enemy in y
# enemy_y = 50
enemy_y = random.randint( 50, 150 )

# change the enemy speed
enemy_x_change = 4

# change the value of rate change in "y"
enemy_y_change = 40

# |||||||| v10_1/6: Create the bullet
# bullet definition
bullet_img = pygame.image.load( "tomato.png" )
bullet_x = 0
bullet_y = 480 # the same x coordinate of spaceship
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

# player function
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# enemy function
def enemy(x, y):
    screen.blit( enemy_img, ( x, y ) )

# |||||||| v10_2/6: create fire function
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    # the initial position of the bullet
    screen.blit( bullet_img, ( x + 16, y + 10 ) )

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
                player_x_change = -5 
                
            if event.key == pygame.K_RIGHT:
                # change the player speed
                player_x_change = 5
            
            # |||||||| v10_3/6: detect space key 
            if event.key == pygame.K_SPACE:
                fire( player_x, bullet_y )


                
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

    # logic for movement of the enemy
    enemy_x += enemy_x_change
    if enemy_x <= 0:

        #change the enemy speed
        enemy_x_change = 4
        enemy_y += enemy_y_change

    # size of the enemy is according 
    # to size of the enemy in px. in this case the enemy
    # size is 24 px, this is: 800 - 24: 776
      
    elif enemy_x >= 776: 
        #change the enemy speed
        enemy_x_change = -4
        
        enemy_y += enemy_y_change

    # ||||||||| v10_4/6: logic for bullet movement
    if bullet_state == "fire":
        # ||||||||| v10_5/6: initial position of the bullet
        fire( player_x, bullet_y )
        #||||||||| v10_6/6: bullet movement
        bullet_y -= bullet_y_change

    
    # add the arguments to function
    player( player_x, player_y )

    # calling to enemy function
    enemy( enemy_x, enemy_y )
    
    # update the window 
    pygame.display.update()
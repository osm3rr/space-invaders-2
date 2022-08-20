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

# Create the bullet
# bullet definition
bullet_img = pygame.image.load( "tomato.png" )
bullet_x = 0
bullet_y = 480 # the same x coordinate of spaceship
bullet_x_change = 0
bullet_y_change = 20
bullet_state = "ready"

# player function
def player(x, y):
    screen.blit( player_img, ( x, y ) )

# enemy function
def enemy(x, y):
    screen.blit( enemy_img, ( x, y ) )

# create fire function
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
                player_x_change = -10 
                
            if event.key == pygame.K_RIGHT:
                # change the player speed
                player_x_change = 10
            
            # detect space key 
            if event.key == pygame.K_SPACE:
                # |||||||| v11_7/7: review the bullet state
                if bullet_state == "ready":    
                    # |||||||| v11_5/7: set bullet_x to player_x
                    bullet_x = player_x
                    # |||||||| v11_6/7: change player_x to bullet_x
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

    # logic for bullet movement

    # ||||||| v11_1/7: logic for multiple bullet
    if bullet_y <= 0: # 0 is the condition for the bullet
        # ||||||| v11_2/7: reset the bullet position
        bullet_y = 480
        # ||||||| v11_3/7: reset the bullet state
        bullet_state = "ready"

    if bullet_state == "fire":
        # |||||||| v11_4/7 set fire function with bullet_x
        # instead player_x
        fire( bullet_x, bullet_y )
        # bullet movement
        bullet_y -= bullet_y_change

    # add the arguments to function
    player( player_x, player_y )

    # calling to enemy function
    enemy( enemy_x, enemy_y )
    
    # update the window 
    pygame.display.update()
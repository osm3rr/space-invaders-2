from nis import match
import pygame 
import random
# ||||||| v12_2/9: math library (line:4)
import math

# initializate pygame
pygame.init()

# windows size
screen_width = 800
screen_height = 600

# ||||||||| v12_9/9: put the images in variables (line:14)
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

# title
pygame.display.set_caption( "Space invaders @adakademy" )

# icon 
icon = pygame.image.load( icon_image )
pygame.display.set_icon( icon )

# player
player_img = pygame.image.load( player_image )
player_x = 370
player_y = 480
# add the rate change in x
player_x_change = 0

# enemy definition
enemy_img = pygame.image.load( alien_image )

# randoom movement of the enemy in x
# enemy_x = 370
# ||||||||| v12_8/9:reset the enemy ubication (line:49)
enemy_x = random.randint( 0, 735 )

# randoom movement of the enemy in y
# enemy_y = 50
enemy_y = random.randint( 50, 150 )

# change the enemy speed
enemy_x_change = 4

# change the value of rate change in "y"
enemy_y_change = 40

# Create the bullet
# bullet definition
bullet_img = pygame.image.load( bullet_image )
bullet_x = 0
bullet_y = 480 # the same x coordinate of spaceship
bullet_x_change = 0
bullet_y_change = 20
bullet_state = "ready"

# |||||||| v12_5/9: score variable (line: 71)
score = 0

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
    screen.blit( bullet_img, ( x + 8, y + 10 ) )

# |||||||| v12_1/9: function to detect the collision ( line:89 )
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

    # logic for movement of the enemy
    enemy_x += enemy_x_change
    if enemy_x <= 0:

        #change the enemy speed
        enemy_x_change = 6
        enemy_y += enemy_y_change

    # size of the enemy is according 
    # to size of the enemy in px. in this case the enemy
    # size is 24 px, this is: 800 - 24: 776
      
    elif enemy_x >= 736: 
        #change the enemy speed
        enemy_x_change = -6
        
        enemy_y += enemy_y_change

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
    
    # ||||||||| v12_3/9: save the result of collision function (line:187 )
    collision = is_collision( enemy_x, enemy_y, bullet_x, bullet_y )
    
    # ||||||||| v12_4/9: is there a collision? ( line:190 )
    if collision:
        bullet_y = 480
        bullet_state = "ready"
        # ||||||||| v12_6/9: increment the score variable ( line:194 )
        score += 1
        # ||||||||| v12_7/9: remove the print() (line:196)
        # print( score )
        # ||||||||| v12_8/9:reset the enemy ubication (line:198)
        enemy_x = random.randint( 0, 735 )
        enemy_y = random.randint( 50, 150 )

    # add the arguments to function
    player( player_x, player_y )

    # calling to enemy function
    enemy( enemy_x, enemy_y )
    
    # update the window 
    pygame.display.update()
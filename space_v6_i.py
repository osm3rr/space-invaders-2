# v1_1: pygame library
import pygame 

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
player_img = pygame.image.load( "player3.png" )
player_x = 370
player_y = 480
# v5_4: add the rate change in x
player_x_change = 0

# v3_2: player function
# def player():
#     screen.blit( player_img, ( player_x, player_y ) )

# v4_1: add in the player function the parameter x and y
def player(x, y):
    screen.blit( player_img, ( x, y ) )



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
    
    #|||||||||||| v6_1/2: player x boundaries left||||||||||
    if player_x <= 0:
        player_x = 0
        
    # |||||||||||| v6_2/2: this value 736, is according to 
    # the size of the player image
    # player boundaries right
    elif player_x >= 736: 
        player_x = 736
    
    # v4_2: add the arguments to function
    player( player_x, player_y )
    
    # v2_4: update the window 
    pygame.display.update()
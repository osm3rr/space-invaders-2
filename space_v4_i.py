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

# v3_2: player function
#////// v4_1: add in the player function the parameter x and y //////
def player(x, y):
    screen.blit( player_img, ( x, y ) )



# v1_6: Game loop
running = True
while running:
    
    # ///// v4_3: for increment the speed in x
    # player_x += 5
    
    # //////v4_4: change the increment the speed in x by 0.1
    #player_x += 0.1
    
    # //////v4_5: change the increment the speed in x by -0.1
    #player_x -= 0.1
    
    # ///// v4_6: for demonstration purposes
    #print(  player_x )
    
    # //////v4_7: change the increment the speed in y by -0.1
    player_y -= 0.1
    
    # ///// v4_8: for demonstration purposes
    print(  player_y )
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # v2_3: RGB -> Red, Green, Blue 
    rgb = ( 0, 0, 0)
    screen.fill( rgb )
    
    # v3_3: player function
    # /////// v4_2: add the arguments to function////
    player( player_x, player_y )
    
    # v2_4: update the window 
    pygame.display.update()


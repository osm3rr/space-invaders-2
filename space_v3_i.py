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

# //// v3_1: player /////
player_img = pygame.image.load( "player3.png" )
player_x = 370
player_y = 480

#///// v3_2: player function ////
def player():
    screen.blit( player_img, ( player_x, player_y ) )



# v1_6: Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # v2_3: RGB -> Red, Green, Blue 
    rgb = ( 0, 0, 0)
    screen.fill( rgb )
    
    # ////// v3_3: player function ////
    player()
    
    # v2_4: update the window 
    pygame.display.update()


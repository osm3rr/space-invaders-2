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

# v1_6: Game loop
running = True
while running:
    for event in pygame.event.get():
        #print( event )
        if event.type == pygame.QUIT:
            running = False
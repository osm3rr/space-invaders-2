import pygame

pygame.init()

# size
screen_width = 800
screen_height = 600

size = ( screen_width, screen_height )

screen = pygame.display.set_mode( size )

# game loop
running = True
while running:
    for event in pygame.event.get():
        #print( event )
        if event.type == pygame.QUIT:
            running = False
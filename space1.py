import pygame

# initializate pygame
pygame.init()

# windows size
screen_width = 800
screen_height = 600

size = ( screen_width, screen_height )

# Display the windows
screen = pygame.display.set_mode( size )

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
import pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill(black)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            quit()
#    pygame.display.flip()
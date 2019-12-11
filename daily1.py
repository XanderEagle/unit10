import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption("Pygame Daily Exercise 1")

main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (255, 255, 100), (50, 50, 200, 100), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((800, 700), 0, 32)

pygame.display.set_caption("Pygame Picture")

main_surface.fill((167, 212, 44))

pygame.draw.ellipse(main_surface, (0, 102, 0), (-100, -40, 500, 250), 0)

pygame.draw.ellipse(main_surface, (0, 102, 0), (200, -40, 500, 250), 0)

pygame.draw.ellipse(main_surface, (0, 102, 0), (400, -40, 500, 250), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

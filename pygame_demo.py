import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption("Pygame Demo - So Cool")

main_surface.fill((255, 255, 255))

pygame.draw.rect(main_surface, (0, 0, 255), (50, 50, 200, 100), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

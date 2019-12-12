import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption("Pygame Exercise 1")

main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (0, 255, 0), ((100, 75), (200, 5), (300, 75), (270, 210), (135, 210)), 0)

pygame.draw.line(main_surface, (0, 0, 255), (120, 62), (180, 62), 4)

pygame.draw.line(main_surface, (0, 0, 255), (180, 62), (120, 112), 2)

pygame.draw.line(main_surface, (0, 0, 255), (120, 112), (180, 112), 4)

pygame.draw.rect(main_surface, (255, 0, 0), (230, 110, 100, 50), 0)

pygame.draw.circle(main_surface, (0, 0, 255), (300, 50), 10, 0)

pygame.draw.ellipse(main_surface, (255, 0, 0), (300, 170, 50, 100), 3)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

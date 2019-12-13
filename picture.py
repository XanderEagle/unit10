import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption("Pygame Picture")

main_surface.fill((167, 212, 44))

pygame.draw.rect(main_surface, (153, 76, 0), (90, 0, 50, 800), 0)
pygame.draw.rect(main_surface, (153, 76, 0), (420, 0, 50, 800), 0)
pygame.draw.rect(main_surface, (153, 76, 0), (725, 0, 50, 800), 0)
pygame.draw.rect(main_surface, (153, 76, 0), (1040, 0, 50, 800), 0)

pygame.draw.ellipse(main_surface, (0, 102, 0), (-150, -40, 500, 250), 0)
pygame.draw.ellipse(main_surface, (0, 102, 0), (200, -40, 500, 250), 0)
pygame.draw.ellipse(main_surface, (0, 102, 0), (500, -40, 500, 250), 0)
pygame.draw.ellipse(main_surface, (0, 102, 0), (800, -40, 500, 250), 0)

pygame.draw.rect(main_surface, (255, 255, 103), (0, 498, 1200, 90), 0)
pygame.draw.ellipse(main_surface, (0, 0, 204), (400, 500, 400, 85), 0)
pygame.draw.rect(main_surface, (255, 128, 0), (0, 588, 1200, 90), 0)
pygame.draw.rect(main_surface, (0, 0, 0), (0, 650, 1200, 90), 0)
pygame.draw.rect(main_surface, (255, 128, 0), (0, 740, 1200, 90), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

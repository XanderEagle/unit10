import pygame, sys
from pygame.locals import *
import target


pygame.init()

main_surface = pygame.display.set_mode((800, 800), 0, 32)

pygame.display.set_caption("Target")

main_surface.fill((255, 255, 255))

my_target = target.Target(main_surface)

my_target.draw_target()


def print_mouse_coordinates(self, position):
    mouse_font = pygame.font._SysFont("Helvetica", 32)
    mouse_label = mouse_font.render(position, 1, (0, 255, 255))
    self.main_surface.blit(mouse_label, (30, 30))


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

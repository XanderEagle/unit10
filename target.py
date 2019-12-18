import pygame


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_target(self):
        x = int(self.main_surface.get_width()/2)
        y = int(self.main_surface.get_height()/2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 350, 1)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 280, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 210, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 150, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 80, 0)
# Xander Eagle
# January 6, 2020
# this program draws a target and adds up the total points based on where the user clicks
import pygame


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.score = 0

    def draw_target(self):   # this functions draws the target and adds the color
        x = int(self.main_surface.get_width()/2)
        y = int(self.main_surface.get_height()/2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 350, 1)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 280, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 210, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 150, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 80, 0)

    def print_mouse_coordinates(self, position):   # this function gives each color a value and adds it up the total...
        # ...every click
        target_color = self.main_surface.get_at(position)
        if target_color == (255, 255, 0, 255):
            self.score += 9
        if target_color == (255, 0, 0, 255):
            self.score += 7
        if target_color == (0, 0, 255, 255):
            self.score += 5
        if target_color == (0, 0, 0, 255):
            self.score += 3
        if target_color == (255, 255, 255, 255):
            self.score += 1
        self.main_surface.fill((255, 255, 255))
        self.draw_target()
        mouse_font = pygame.font.SysFont("Helvetica", 32)
        mouse_label = mouse_font.render(str(self.score), 1, (0, 255, 255))
        self.main_surface.blit(mouse_label, (30, 30))

        pygame.display.update()

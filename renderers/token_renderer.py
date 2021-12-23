import pygame

from engine.renderer import Renderer


class TokenRenderer(Renderer):
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

    def switch_color(self, new_color):
        self.color = new_color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size)

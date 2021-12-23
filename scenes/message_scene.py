import pygame

from engine.scene import Scene


class MessageScene(Scene):
    def __init__(self, surface):
        self.surface = surface

    def handle_events(self, event):
        pass

    def render(self):
        self.surface.fill(pygame.Color("red"))

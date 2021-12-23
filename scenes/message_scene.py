import pygame

from engine.scene import Scene


class MessageScene(Scene):
    def __init__(self, surface, message):
        super().__init__(surface)
        self.message = message
        self.font = pygame.font.SysFont(None, 24)

    def handle_events(self, event):
        pass

    def render(self):
        self.surface.fill(pygame.Color("red"))

        img = self.font.render(self.message, True, pygame.Color("black"))
        self.surface.blit(img, (20, 20))

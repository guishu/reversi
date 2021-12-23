import pygame

from engine.scene import Scene


class MessageScene(Scene):
    def __init__(self, surface, message, fore_color, back_color):
        super().__init__(surface)
        self.background_color = back_color
        self.text_surface, self.text_pos = self._prepare_text(message, fore_color)

    def _prepare_text(self, message, color):
        self.font = pygame.font.SysFont(None, 24)
        text_surface = self.font.render(message, True, color)

        full_width, full_height = self.surface.get_size()
        text_width, text_height = text_surface.get_size()

        x = (full_width - text_width) // 2
        y = (full_height - text_height) // 2

        return text_surface, (x, y)

    def handle_events(self, event):
        pass

    def render(self):
        self.surface.fill(self.background_color)

        self.surface.blit(self.text_surface, self.text_pos)

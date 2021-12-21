import pygame

from model.game import Game
from renderers.board_renderer import BoardRenderer


class GameScene:
    def __init__(self, surface):
        self.surface = surface
        self.game = Game()
        self.board_renderer = BoardRenderer(self.game, surface.get_size())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = self.board_renderer.get_cell(event.pos)
            if not self.game.play(x, y):
                return False

        return True

    def render(self):
        self.surface.fill(pygame.Color("burlywood"))
        self.board_renderer.render(self.surface)

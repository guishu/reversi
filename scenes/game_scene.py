import pygame

from engine import scene_manager as sm
from engine.scene import Scene
from model.game import Game
from renderers.board_renderer import BoardRenderer
from scenes.message_scene import MessageScene


class GameScene(Scene):
    def __init__(self, surface):
        super().__init__(surface)
        self.game = Game()
        self.board_renderer = BoardRenderer(self.game, surface.get_size())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = self.board_renderer.get_cell(event.pos)
            if not self.game.play(x, y):
                sm.scenes.remove(self)
                sm.scenes.insert(0, MessageScene(self.surface, "Game over", fore_color=pygame.Color("black"), back_color=pygame.Color("white")))

    def render(self):
        self.surface.fill(pygame.Color("burlywood"))
        self.board_renderer.render(self.surface)

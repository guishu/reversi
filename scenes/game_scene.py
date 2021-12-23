import pygame

from engine import scene_manager as sm
from engine.scene import Scene
from model.game import Game
from model.board import TOKEN_CREATED_EVENT, TOKEN_SWITCHED_EVENT
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
                self._game_over()
        elif event.type == TOKEN_CREATED_EVENT:
            self.board_renderer.on_new_token(event.pos, event.color)
        elif event.type == TOKEN_SWITCHED_EVENT:
            self.board_renderer.on_token_switch(event.pos, event.color)

    def render(self):
        self.surface.fill(pygame.Color("burlywood"))
        self.board_renderer.render(self.surface)

    def _game_over(self):
        score = self.game.get_score()

        if score[0] > score[1]:
            message = f"Blanc gagne {score[0]} à {score[1]}."
        elif score[1] > score[0]:
            message = f"Noir 2 gagne {score[1]} à {score[0]}."
        else:
            message = f"Match nul, {score[0]} partout."

        sm.scenes.remove(self)
        sm.scenes.insert(0, MessageScene(
            self.surface,
            message,
            fore_color=pygame.Color("black"),
            back_color=pygame.Color("white"))
        )

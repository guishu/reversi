import pygame

from engine.renderer import Renderer
from renderers.token_renderer import TokenRenderer


class BoardRenderer(Renderer):
    """
    Handles board rendering and everything related to board on screen
    """

    def __init__(self, game, area_size):
        """
        Constructor
        :param board: The board model rendered by this instance
        :param area_size: The size of the area on screen
        """
        self.game = game

        self.background_color = pygame.Color("green4")
        self.foreground_color = pygame.Color("black")

        self.player0_color = pygame.Color("white")
        self.player1_color = pygame.Color("black")

        self.tile_size = BoardRenderer._compute_tile_size(area_size)

        self.font = pygame.font.SysFont(None, 24)

        self.size = 8 * self.tile_size
        self.pos = (
                (area_size[0] - self.size) // 2,
                (area_size[1] - self.size) // 2,
        )

        self.tokens = {}
        self._prepare_turn_tokens()

    def render(self, surface):
        """
        Renders the board and its tokens on screen
        :param surface: The surface (screen) to render on
        """
        surface.fill(self.background_color, self.pos + (self.size, self.size))

        left = self.pos[0]
        top = self.pos[1]
        right = left + self.size
        bottom = top + self.size

        for i in range(1, 8):
            offset = self.tile_size * i
            pygame.draw.line(surface, self.foreground_color, (left + offset, top), (left + offset, bottom))
            pygame.draw.line(surface, self.foreground_color, (left, top + offset), (right, top + offset))

        for token in self.tokens.values():
            token.render(surface)

        self._draw_turn(surface)

    def get_cell(self, pos):
        """
        Retrieves the cell coordinates at given screen position
        :param pos: The screen position
        :return: A tuple (x, y) in board coordinates. Component is -1 if out of the board.
        """
        x = -1
        if self.pos[0] <= pos[0] <= self.pos[0] + self.size:
            x = (pos[0] - self.pos[0]) // self.tile_size
        y = -1
        if self.pos[1] <= pos[1] <= self.pos[1] + self.size:
            y = (pos[1] - self.pos[1]) // self.tile_size

        return x, y

    def on_new_token(self, pos, color):
        if color == 0:
            token_color = self.player0_color
        else:
            token_color = self.player1_color

        token_x = self.pos[0] + self.tile_size * (pos[0] + 0.5)
        token_y = self.pos[1] + self.tile_size * (pos[1] + 0.5)
        token_size = self.tile_size * 0.4

        self.tokens[pos] = TokenRenderer((token_x, token_y), token_size, token_color)

    def on_token_switch(self, pos, color):
        if color == 0:
            token_color = self.player0_color
        else:
            token_color = self.player1_color

        self.tokens[pos].switch_color(token_color)

    @staticmethod
    def _compute_tile_size(area_size):
        """
        Computes ideal tile size for given surface size
        :param area_size: The area size the board should fit in
        :return: Ideal tile size
        """
        smallest = min(area_size[0], area_size[1])

        return smallest // 8

    def _prepare_turn_tokens(self):
        tok_x = self.pos[0] // 2
        tok_y = self.pos[1] + self.size // 2
        tok_radius = self.tile_size * 0.4
        self.tokens[(-1, -1)] = TokenRenderer((tok_x, tok_y), tok_radius, self.player0_color)

        tok_x += self.pos[0] + self.size
        self.tokens[(-2, -2)] = TokenRenderer((tok_x, tok_y), tok_radius, self.player1_color)

    def _draw_turn(self, surface):
        score = self.game.get_score()

        token_0 = self.tokens[(-1, -1)]
        token_1 = self.tokens[(-2, -2)]

        if self.game.to_play == 0:
            pygame.draw.circle(surface, pygame.Color("red"), token_0.pos, token_0.size + 3, width=3)
        else:
            pygame.draw.circle(surface, pygame.Color("red"), token_1.pos, token_1.size + 3, width=3)

        self._draw_score(surface, token_0.pos, score[0], self.player1_color)
        self._draw_score(surface, token_1.pos, score[1], self.player0_color)

    def _draw_score(self, surface, pos_center, score, color):
        text = self.font.render(str(score), True, color)
        text_width, text_height = text.get_size()
        x = pos_center[0] - text_width // 2
        y = pos_center[1] - text_height // 2
        surface.blit(text, (x, y))

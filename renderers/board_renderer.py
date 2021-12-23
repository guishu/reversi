import pygame

from engine.renderer import Renderer


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
        self.board = game.board

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

        for x in range(0, 8):
            for y in range(0, 8):
                token = self.board.get_token(x, y)
                if token != -1:
                    self._render_token(surface, token, x, y)

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

    @staticmethod
    def _compute_tile_size(area_size):
        """
        Computes ideal tile size for given surface size
        :param area_size: The area size the board should fit in
        :return: Ideal tile size
        """
        smallest = min(area_size[0], area_size[1])

        return smallest // 8

    def _render_token(self, surface, player, x, y):
        """
        Renders a token on screen
        :param surface: Surface to render on
        :param player: Player index (0 or 1)
        :param x: The x board coordinate to render on
        :param y: The y board coordinate to render on
        """
        if player == 0:
            color = self.player0_color
        else:
            color = self.player1_color

        pygame.draw.circle(
            surface,
            color,
            (self.pos[0] + self.tile_size * (x + 0.5), self.pos[1] + self.tile_size * (y + 0.5)),
            self.tile_size * 0.4)

    def _draw_turn(self, surface):
        score = self.board.get_score()

        tok_x = self.pos[0] // 2
        tok_y = self.pos[1] + self.size // 2
        tok_radius = self.tile_size * 0.4
        pygame.draw.circle(surface, self.player0_color, (tok_x, tok_y), tok_radius)
        if self.game.to_play == 0:
            pygame.draw.circle(surface, pygame.Color("red"), (tok_x, tok_y), tok_radius + 3, width=3)
        self._draw_score(surface, (tok_x, tok_y), score[0], self.player1_color)

        tok_x += self.pos[0] + self.size
        pygame.draw.circle(surface, self.player1_color, (tok_x, tok_y), tok_radius)
        if self.game.to_play == 1:
            pygame.draw.circle(surface, pygame.Color("red"), (tok_x, tok_y), tok_radius + 3, width=3)
        self._draw_score(surface, (tok_x, tok_y), score[1], self.player0_color)

    def _draw_score(self, surface, pos_center, score, color):
        text = self.font.render(str(score), True, color)
        text_width, text_height =  text.get_size()
        x = pos_center[0] - text_width // 2
        y = pos_center[1] - text_height // 2
        surface.blit(text, (x, y))

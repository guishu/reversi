import pygame


class BoardRenderer:
    """
    Handles board rendering and everything related to board on screen
    """

    def __init__(self, board, area_size):
        """
        Constructor
        :param board: The board model rendered by this instance
        :param area_size: The size of the area on screen
        """
        self.board = board

        self.background_color = pygame.Color("green4")
        self.foreground_color = pygame.Color("black")

        self.player0_color = pygame.Color("white")
        self.player1_color = pygame.Color("black")

        self.tile_size = BoardRenderer._compute_tile_size(area_size)

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

    def get_cell(self, pos):
        """
        Retreives the cell coordinates at given screen position
        :param pos: The screen position
        :return: A tuple (x, y) in board coordinates
        """
        x = -1
        if pos[0] >= self.pos[0] <= self.pos[0] + self.size:
            x = (pos[0] - self.pos[0]) // self.tile_size
        y = -1
        if pos[1] >= self.pos[1] <= self.pos[1] + self.size:
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

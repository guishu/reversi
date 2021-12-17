import pygame

class BoardRenderer:
    def __init__(self, area_size):
        self.background_color = pygame.Color("green4")
        self.foreground_color = pygame.Color("black")

        self.tile_size = BoardRenderer._compute_tile_size(area_size)

        self.size = 8 * self.tile_size
        self.pos = (
                (area_size[0] - self.size) // 2,
                (area_size[1] - self.size) // 2,
        )

    @staticmethod
    def _compute_tile_size(area_size):
        smallest = min(area_size[0], area_size[1])

        return smallest // 8

    def render(self, surface):
        surface.fill(self.background_color, self.pos + (self.size, self.size))

        left = self.pos[0]
        top = self.pos[1]
        right = left + self.size
        bottom = top + self.size

        for i in range(1, 8):
            offset = self.tile_size * i
            pygame.draw.line(surface, self.foreground_color, (left + offset, top), (left + offset, bottom))
            pygame.draw.line(surface, self.foreground_color, (left, top + offset), (right, top + offset))

    def render_token(self, surface, player, x, y):
        if player == 0:
            color = pygame.Color("white")
        else:
            color = pygame.Color("black")

        pygame.draw.circle(
            surface,
            color,
            (self.pos[0] + self.tile_size * (x + 0.5), self.pos[1] + self.tile_size * (y + 0.5)),
            self.tile_size * 0.4)
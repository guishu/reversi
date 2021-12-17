import pygame

from renderers.board_renderer import BoardRenderer
from model.board import Board


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    board = Board()
    board.set_start_position()
    board_renderer = BoardRenderer(board, screen.get_size())

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color("black"))

        board_renderer.render(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

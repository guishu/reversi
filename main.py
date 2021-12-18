import pygame

from renderers.board_renderer import BoardRenderer
from model.game import Game


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    game = Game()
    board_renderer = BoardRenderer(game.board, screen.get_size())

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = board_renderer.get_cell(event.pos)
                game.play(x, y)

        screen.fill(pygame.Color("black"))

        board_renderer.render(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

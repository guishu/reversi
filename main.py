import pygame

from renderers.board_renderer import BoardRenderer


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    board_renderer = BoardRenderer(screen.get_size())

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color("black"))

        board_renderer.render(screen)

        board_renderer.render_token(screen, 0, 3, 3)
        board_renderer.render_token(screen, 0, 4, 4)
        board_renderer.render_token(screen, 1, 3, 4)
        board_renderer.render_token(screen, 1, 4, 3)

        pygame.display.flip()


if __name__ == "__main__":
    main()

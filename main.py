import pygame

from scenes.game_scene import GameScene


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    game_scene = GameScene(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                running = game_scene.handle_events(event)

        game_scene.render()

        pygame.display.flip()


if __name__ == "__main__":
    main()

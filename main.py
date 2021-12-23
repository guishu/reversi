import pygame

from engine import scene_manager as sm
from scenes.game_scene import GameScene


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    sm.scenes.append(GameScene(screen))

    while sm.scenes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.scenes = []
            else:
                for scene in sm.scenes:
                    scene.handle_events(event)

        for scene in sm.scenes:
            scene.render()

        pygame.display.flip()


if __name__ == "__main__":
    main()

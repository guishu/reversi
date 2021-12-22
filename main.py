import pygame

from engine.scene import Scene
from scenes.game_scene import GameScene


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    scenes = [GameScene(screen)]

    while scenes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scenes = []
            else:
                for scene in scenes:
                    result = scene.handle_events(event)
                    if not result:
                        scenes.remove(scene)
                    elif type(result) == Scene:
                        scenes.insert(0, result)

        for scene in scenes:
            scene.render()

        pygame.display.flip()


if __name__ == "__main__":
    main()

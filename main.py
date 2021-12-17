import pygame


class Board:
    def __init__(self):
        self.background_color = pygame.Color("green4")
        self.pos = (0, 0)
        self.size = (400, 400)


def main():
    pygame.init()

    pygame.display.set_caption("Reversi")

    screen = pygame.display.set_mode((800, 600))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color("black"))

        screen.fill(pygame.Color("green4"), (144, 44, 512, 512))

        for i in range(1, 8):
            pygame.draw.line(screen, pygame.Color("black"), (144 + 64 * i, 44), (144 + 64 * i, 556))
            pygame.draw.line(screen, pygame.Color("black"), (144, 44 + 64 * i), (656 + 64 * i, 44 + 64 * i))

        pygame.draw.circle(screen, pygame.Color("white"), (144 + 64 * 3 + 32, 44 + 64 * 3 + 32), 27)
        pygame.draw.circle(screen, pygame.Color("white"), (144 + 64 * 4 + 32, 44 + 64 * 4 + 32), 27)
        pygame.draw.circle(screen, pygame.Color("black"), (144 + 64 * 3 + 32, 44 + 64 * 4 + 32), 27)
        pygame.draw.circle(screen, pygame.Color("black"), (144 + 64 * 4 + 32, 44 + 64 * 3 + 32), 27)

        pygame.display.flip()


if __name__ == "__main__":
    main()

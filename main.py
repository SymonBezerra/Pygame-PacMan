import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

if __name__ == "__main__":
    pygame.init()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
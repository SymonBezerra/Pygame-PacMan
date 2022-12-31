import pygame
from scenario import Scenario
from wall import Wall

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

game_scenario = Scenario()

def blit_scenario():
    INIT_COORDS = (400,0)
    tile: Wall
    for tile in game_scenario.tiles:
        screen.blit(tile.image,
        tile.rect(INIT_COORDS + (20 * tile.coordinate[0]),
        INIT_COORDS + (20 * tile.coordinate[1])))

if __name__ == "__main__":
    pygame.init()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    blit_scenario()
    
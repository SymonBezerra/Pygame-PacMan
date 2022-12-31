import pygame
from scenario import Scenario, GAME_MAP
from wall import Wall, WALL_SIZE

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pac-Man")

game_scenario = Scenario()

def blit_scenario():
    INIT_COORDS = (200,50)
    tile: Wall
    for tile in game_scenario.tiles:
        tile_coord = (INIT_COORDS[0] + (WALL_SIZE * tile.coordinate[0]),
        INIT_COORDS[1] + (WALL_SIZE * tile.coordinate[1]))

        tile.rect = tile.image.get_rect(center=tile_coord)

        screen.blit(tile.image, tile.rect)
if __name__ == "__main__":
    pygame.init()
    print(GAME_MAP)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        blit_scenario()

        pygame.display.flip()
import pygame
from scenario import Scenario, GAME_MAP
from wall import Wall, WALL_SIZE
from pac_man import PacMan

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pac-Man")

game_scenario = Scenario()

def blit_scenario() -> None:
    INIT_COORDS = (200,50)
    tile: Wall
    for tile in game_scenario.tiles:
        tile_coord = (INIT_COORDS[0] + (WALL_SIZE * tile.coordinate[0]),
        INIT_COORDS[1] + (WALL_SIZE * tile.coordinate[1]))

        tile.rect = tile.image.get_rect(center=tile_coord)

        screen.blit(tile.image, tile.rect)

pac_man = PacMan()

if __name__ == "__main__":
    pygame.init()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pac_man.refresh("UP")
                elif event.key == pygame.K_DOWN:
                    pac_man.refresh("DOWN")
                elif event.key == pygame.K_LEFT:
                    pac_man.refresh("LEFT")
                elif event.key == pygame.K_RIGHT:
                    pac_man.refresh("RIGHT")

        blit_scenario()
        pac_man.show(screen)

        pygame.display.flip()
import pygame
from scenario import Scenario, GAME_MAP
from wall import Wall, WALL_SIZE
from pac_man import PacMan
from ghost import Ghost

screen = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Pac-Man")

game_scenario = Scenario()

def blit_scenario() -> None:
    INIT_COORDS = (100,50)
    tile: Wall
    for tile in game_scenario.tiles:
        tile_coord = (INIT_COORDS[0] + (WALL_SIZE * tile.coordinate[0]),
        INIT_COORDS[1] + (WALL_SIZE * tile.coordinate[1]))

        tile.rect = tile.image.get_rect(center=tile_coord)

        screen.blit(tile.image, tile.rect)

pac_man = PacMan()
blinky = Ghost("Blinky", (320, 300))

if __name__ == "__main__":
    pygame.init()

    running = True

    while running:

        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pac_man.move = "UP"
                elif event.key == pygame.K_DOWN:
                    pac_man.move = "DOWN"
                elif event.key == pygame.K_LEFT:
                    pac_man.move = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pac_man.move = "RIGHT"

        blit_scenario()
        pac_man.show(screen)
        blinky.show(screen)

        pac_man.refresh(game_scenario)
        
        CLOCK.tick(20)
        pygame.display.flip()
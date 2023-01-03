import pygame
from scenario import Scenario
from wall import Wall

SPEED = 5

class PacMan (pygame.sprite.Sprite):

    def __init__ (self):
        super(PacMan, self).__init__()

        self.image = pygame.image.load("gfx/pacman_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,20))
        
        self.rect = self.image.get_rect()

        self.move = "RIGHT"

        self.coordinate = [300, 300]

    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(center=(self.coordinate))
        screen.blit(self.image, self.rect)

    # collision detection
    def refresh (self, scenario: Scenario) -> bool:
        tile: Wall
        new_rect = []
        collision_check = []
        if self.move == "UP":
            new_rect = [self.coordinate[0], self.coordinate[1] - SPEED]
            collision_check = [self.coordinate[0], self.coordinate[1] - SPEED * 4]
        elif self.move == "DOWN":
            new_rect = [self.coordinate[0], self.coordinate[1] + SPEED]
            collision_check = [self.coordinate[0], self.coordinate[1] + SPEED * 4]
        elif self.move == "LEFT":
            if self.coordinate[0] < 200:
                new_rect = [680, self.coordinate[1]]
                collision_check = [680, self.coordinate[1]]
            else:
                new_rect = [self.coordinate[0] - SPEED, self.coordinate[1]]
                collision_check = [self.coordinate[0] - SPEED * 4, self.coordinate[1]]
        elif self.move == "RIGHT":
            if self.coordinate[0] > 680:
                new_rect = [200, self.coordinate[1]]
                collision_check = [200, self.coordinate[1]]
            else:
                new_rect = [self.coordinate[0] + SPEED, self.coordinate[1]]
                collision_check = [self.coordinate[0] + SPEED * 4, self.coordinate[1]]

        for tile in scenario.tiles:
            if tile.rect.collidepoint(new_rect[0], collision_check[1]):
                if tile.type != 0:
                    return False
                else:
                    scenario.tiles.remove(tile)
        
        self.coordinate = new_rect
        return True
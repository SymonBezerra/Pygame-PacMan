import pygame
from scenario import Scenario
from wall import Wall

GHOSTS = {"Blinky": "gfx/blinky_1.png"}
SPEED = 5

class Ghost (pygame.sprite.Sprite):

    def __init__ (self, name: str, coordinate: tuple): 
        # Blinky (red), Pinky(pink), Inky(blue) and Clyde(yellow)
        self.name = name
        self.coordinate = coordinate
        
        self.image = pygame.image.load(GHOSTS[self.name]).convert_alpha()

        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect(center=(self.coordinate))

    
    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(center=(self.coordinate))
        screen.blit(self.image, self.rect)

    def refresh (self, scenario: Scenario) -> bool:
        tile: Wall
        new_rect = []
        collision_check = []
        if self.move == "UP":
            new_rect = [self.coordinate[0], self.coordinate[1] - SPEED]
            collision_check = [self.coordinate[0], self.coordinate[1] - SPEED * 3]
        elif self.move == "DOWN":
            new_rect = [self.coordinate[0], self.coordinate[1] + SPEED]
            collision_check = [self.coordinate[0], self.coordinate[1] + SPEED * 3]
        elif self.move == "LEFT":
            if self.coordinate[0] < 100:
                new_rect = [580, self.coordinate[1]]
                collision_check = [580, self.coordinate[1]]
            else:
                new_rect = [self.coordinate[0] - SPEED, self.coordinate[1]]
                collision_check = [self.coordinate[0] - SPEED * 3, self.coordinate[1]]
        elif self.move == "RIGHT":
            if self.coordinate[0] > 580:
                new_rect = [100, self.coordinate[1]]
                collision_check = [100, self.coordinate[1]]
            else:
                new_rect = [self.coordinate[0] + SPEED, self.coordinate[1]]
                collision_check = [self.coordinate[0] + SPEED * 3, self.coordinate[1]]

        for tile in scenario.tiles:
            if tile.rect.collidepoint(collision_check[0], collision_check[1]):
                if tile.type not in (0,2):
                    return False
                else:
                    scenario.tiles.remove(tile)
                    if tile.type == 2:
                        self.countdown = 200
        
        self.coordinate = new_rect
        return True

class Blinky (Ghost):

    def __init__ (self, coordinate: tuple):
        self.coordinate = coordinate
        super().__init__("Blinky", coordinate)
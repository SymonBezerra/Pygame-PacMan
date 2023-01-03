import pygame
from scenario import Scenario
from wall import Wall

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

    def refresh (self, scenario: Scenario) -> bool:
        tile: Wall
        new_rect = []
        if self.move == "UP":
            new_rect = [self.coordinate[0], self.coordinate[1] - 5]
        elif self.move == "DOWN":
            new_rect = [self.coordinate[0], self.coordinate[1] + 5]
        elif self.move == "LEFT":
            new_rect = [self.coordinate[0] - 5, self.coordinate[1]]
        elif self.move == "RIGHT":
            new_rect = [self.coordinate[0] + 5, self.coordinate[1]]
        for tile in scenario.tiles:
            if tile.rect.collidepoint(new_rect[0], new_rect[1]) and tile.type != 0:
                return False
        
        self.coordinate = new_rect
        return True
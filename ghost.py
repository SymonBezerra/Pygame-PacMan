import pygame
from scenario import Scenario
from wall import Wall
from pac_man import PacMan
from random import randint

GHOSTS = {"Blinky": "gfx/blinky_1.png"}
SPEED = 5

class Ghost (pygame.sprite.Sprite):

    def __init__ (self, name: str, coordinate: tuple): 
        # Blinky (red), Pinky(pink), Inky(blue) and Clyde(yellow)
        self.name = name
        self.coordinate = coordinate
        
        self.direction = "RIGHT"
        self.image = pygame.image.load(GHOSTS[self.name]).convert_alpha()

        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect(center=(self.coordinate))

    
    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(center=(self.coordinate))
        screen.blit(self.image, self.rect)
        

            

# class Blinky (Ghost):

#     def __init__ (self, coordinate: tuple):
#         self.coordinate = coordinate
#         super().__init__("Blinky", coordinate)

#         self.mode = "CHASE"
#         self.direction = "UP"

#     def move (self, pac_man: PacMan) -> None:

#         if self.mode == "CHASE":
#             target = pac_man.coordinate

#     def refresh (self, pac_man: PacMan, scenario: Scenario):
#         self.move(pac_man)
#         super().refresh(scenario)
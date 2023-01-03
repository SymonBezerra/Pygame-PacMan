import pygame

GHOSTS = {"Blinky": "gfx/blinky_1.png"}

class Ghost (pygame.sprite.Sprite):

    def __init__ (self, name: str, init_coord: tuple): 
        # Blinky (red), Pinky(pink), Inky(blue) and Clyde(yellow)
        self.name = name
        
        self.image = pygame.image.load(self.name).convert_alpha()

        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect(center=(init_coord))
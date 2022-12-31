import pygame

WALL_SPRITES = {1: "gfx/wall_vertical"}

class Wall (pygame.sprite.Sprite):

    def __init__ (self, coordinate: tuple, 
    type: int) -> pygame.sprite.Sprite:
        self.coordinate = coordinate
        
        self.image: pygame.image = pygame.image.load(WALL_SPRITES[type]).convert_alpha()
        self.image = pygame.transform.scale((50, 50))
        self.rect = self.image.get_rect()
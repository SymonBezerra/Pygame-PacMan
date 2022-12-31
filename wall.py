import pygame

WALL_SPRITES = {0: "gfx/food_sprite.png",
1: "gfx/top_horizontal_wall.png",
2: "gfx/wall_vertical.png",
3: "gfx/bottom_horizontal_wall.png"}

class Wall (pygame.sprite.Sprite):

    def __init__ (self, coordinate: tuple, 
    type: int) -> pygame.sprite.Sprite:
        self.coordinate = coordinate
        
        self.image: pygame.image = pygame.image.load(WALL_SPRITES[type]).convert_alpha()
        self.image = pygame.transform.scale((20, 20))
        self.rect = self.image.get_rect()
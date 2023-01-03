import pygame

WALL_SIZE = 25

WALL_SPRITES = {0: "gfx/food_sprite.png",
1: "gfx/wall_sprite.png",
2: "gfx/special_sprite.png",
3: "gfx/wall_sprite.png"}

class Wall (pygame.sprite.Sprite):

    def __init__ (self, coordinate: tuple, 
    type: int) -> pygame.sprite.Sprite:
        super(Wall, self).__init__()
        self.coordinate = coordinate

        self.type = type
        
        self.sprite = WALL_SPRITES[type]

        self.image = pygame.image.load(self.sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, 
                                (WALL_SIZE, WALL_SIZE))
        self.rect = self.image.get_rect()
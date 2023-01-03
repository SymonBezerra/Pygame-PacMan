import pygame
from scenario import Scenario
from wall import Wall
FRAMES = {0: "gfx/pacman_idle.png",
1: "gfx/pacman_1.png",
2: "gfx/pacman_2.png",
3: "gfx/pacman_3.png",
4: "gfx/pacman_4.png",
5: "gfx/pacman_3.png",
6: "gfx/pacman_2.png",
7: "gfx/pacman_1.png"}

SPEED = 5

class PacMan (pygame.sprite.Sprite):

    def __init__ (self):
        super(PacMan, self).__init__()

        self.frame = 0

        self.countdown = 0

        self.image = pygame.image.load(FRAMES[self.frame]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,20))
        
        self.rect = self.image.get_rect()

        self.move = "RIGHT"

        self.coordinate = [320, 350]

    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(center=(self.coordinate))
        screen.blit(self.image, self.rect)

    # collision detection
    def refresh (self, scenario: Scenario) -> bool:

        # sprite animation
        if self.frame < 7:
            self.frame += 1
        else: self.frame = 0
        self.image = pygame.image.load(FRAMES[self.frame]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25,25))

        # pacman invincible
        if self.countdown > 0:
            self.countdown -= 1

        # checking collisions

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
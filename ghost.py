import pygame
from scenario import Scenario
from wall import Wall, WALL_SIZE
from pac_man import PacMan
from random import randint

GHOSTS = {"Blinky": "gfx/blinky_1.png"}
SPEED = 5

class Ghost (pygame.sprite.Sprite):

    def __init__ (self, name: str, x: int, y: int):
        # Blinky (red), Pinky(pink), Inky(blue) and Clyde(yellow)
        self.name = name
        self.x = x
        self.y = y
        self.speed = 5

        self.direction = "RIGHT"
        self.image = pygame.image.load(GHOSTS[self.name]).convert_alpha()

        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect(left=self.x, top=self.y)


    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(left=self.x, top=self.y)
        screen.blit(self.image, self.rect)

class Blinky (Ghost):

    def __init__ (self, coordinate: tuple):
         super().__init__("Blinky", coordinate[0], coordinate[1])

         self.mode = "CHASE"
         self.direction = "UP"

    def move (self, pac_man: PacMan, scenario: Scenario) -> None:
        def sort(directions):
            for i in range(len(directions)):
                for j in range(i + 1, len(directions)):
                    if directions[j]['dist'] < directions[i]['dist']:
                        temp = directions[j]
                        directions[j] = directions[i]
                        directions[i] = temp

        if self.mode == "CHASE":
            target = pac_man.coordinate
            directions = self.__choose_direction(target, scenario)
            sort(directions)

            rect = pygame.Rect(0, 0, 0, 0)
            x_speed, y_speed = 0, 0
            for direction in directions:
                if direction['direction'] == 'UP':
                    rect = pygame.Rect(WALL_SIZE, WALL_SIZE, self.x, self.y - WALL_SIZE)
                    x_speed, y_speed = 0, self.speed * -1
                elif direction['direction'] == 'DOWN':
                    rect = pygame.Rect(WALL_SIZE, WALL_SIZE, self.x, self.y + WALL_SIZE)
                    x_speed, y_speed = 0, self.speed
                elif direction['direction'] == 'LEFT':
                    rect = pygame.Rect(WALL_SIZE, WALL_SIZE, self.x - WALL_SIZE, self.y)
                    x_speed, y_speed = self.speed * -1, 0
                elif direction['direction'] == 'RIGHT':
                    rect = pygame.Rect(WALL_SIZE, WALL_SIZE, self.x + WALL_SIZE, self.y)
                    x_speed, y_speed = self.speed, 0
                for tile in scenario.tiles:
                    if tile.rect.collidepoint(self.x + x_speed, self.y + y_speed) and tile.type == 0:
                        self.x += x_speed
                        self.y += y_speed
                        self.direction = direction['direction']
                        return

    def __choose_direction(self, target, scenario: Scenario) -> str:
        directions = {}
        distances = []
        MIN_X, MAX_X = 100, 100 + (25*21)
        MIN_Y, MAX_Y = 50, 50 + (25*20)
        distance = lambda g_pos, t_pos: (g_pos[0] - t_pos[0]) ** 2 + (g_pos[1] - t_pos[1]) ** 2

        if self.direction != 'UP' and self.y + WALL_SIZE <= MAX_Y:
            directions['DOWN'] = (self.x, self.y + WALL_SIZE)
        if self.direction != 'DOWN' and self.y - WALL_SIZE >= MIN_Y:
            directions['UP'] = (self.x, self.y - WALL_SIZE)
        if self.direction != 'LEFT' and self.x + WALL_SIZE <= MAX_X:
            directions['RIGHT'] = (self.x + WALL_SIZE, self.y)
        if self.direction != 'RIGHT' and self.x - WALL_SIZE >= MIN_X:
            directions['LEFT'] = (self.x - WALL_SIZE, self.y)

        for direction in directions:
            dist = distance(directions[direction], target)
            distances.append({'direction': direction, 'dist': dist})

        return distances
    def refresh (self, pac_man, scenario: Scenario):
        self.move(pac_man, scenario)

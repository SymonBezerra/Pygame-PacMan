import csv
import pygame
from wall import Wall

with open ("game_map.csv", newline="") as map:
    reader = csv.reader(map)
    GAME_MAP = [tile for tile in reader]

MAP_SIZE = (20,25) #x, y axis

# print(GAME_MAP)
# the game map will only be used to set up
# the map when in gameplay...

class Scenario:

    def __init__ (self):
        self.tiles = pygame.sprite.Group()
        self.start_scenario()
    
    def start_scenario (self):
        for row in range(MAP_SIZE[0]):
            for column in range(MAP_SIZE[1]):
                if GAME_MAP[column][row] not in ("-", 0):
                    tile = Wall((row,column),
                    int(GAME_MAP[column][row]))
                    self.tiles.add(tile)
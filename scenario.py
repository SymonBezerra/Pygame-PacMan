import csv
import pygame


with open ("game_map.csv", newline="") as map:
    reader = csv.reader(map)
    GAME_MAP = [tile for tile in reader]

# print(GAME_MAP)
# the game map will only be used to set up
# the map when in gameplay...
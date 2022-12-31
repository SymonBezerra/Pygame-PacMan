import csv

with open ("game_map.csv", newline="") as map:
    reader = csv.reader(map)
    GAME_MAP = [tile for tile in reader]

# print(GAME_MAP)
import csv
from player import *

player_list = []

def save():
    pass

with open('resources/players.csv', 'r') as file:
    reader = csv.reader(file)
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            continue

        player_list.append(Player(row[0],
                                  Instrument[row[1]],
                                  Role[row[2]],
                                  Employment[row[3]]))

for player in player_list:
    print(player)

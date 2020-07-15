import csv
from player import *

player_list = []


def save():
    pass


with open('../resources/players.csv', 'r') as file:
    reader = csv.reader(file)
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            continue

        sec_role = []
        if row[4]:
            import_roles = row[4].split(sep=",")
            for role in import_roles:
                try:
                    sec_role.append(Role[role])
                except KeyError:
                    print(f"foreign sec role found in import of {row[0]}")

        player_list.append(Player(row[0],
                                  Instrument[row[1]],
                                  Role[row[2]],
                                  Employment[row[3]],
                                  sec_role))

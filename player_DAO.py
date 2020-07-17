import csv
from player import *
from display_utils import render_columns, split_column


def save():
    with open(file_str, 'w') as file:
        for player in player_list:
            row = [
                player.name,
                player.instrument.name,
                player.prim_role.name,
                player.emp.name,
                player.sec_role[0].name
            ]
            writer = csv.writer(file)
            writer.writerow(row)


player_list = []
revalidate = False
file_str = '../resources/players.csv'


with open(file_str, 'r') as file:
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

        try:
            player_list.append(Player(row[0],
                                      Instrument[row[1]],
                                      Role[row[2]],
                                      Employment[row[3]],
                                      sec_role))
        except:
            print(f"invalid state of object. Player not imported.")
            revalidate = True


if revalidate:
    save()

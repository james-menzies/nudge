import csv
import sys
from pathlib import Path

from player import *
from sys import argv


def save():
    if "--demo" in argv:
        print("[In demo mode, changes will not be saved]")
        return

    with open(file_path, 'w') as file:
        file.write("name,instrument,primary_role,employment_type,secondary_roles\n")
        writer = csv.writer(file, lineterminator='\n')
        for player in player_list:

            row = [
                player.name,
                player.instrument.name,
                player.prim_role.name,
                player.emp.name,
                player.get_sec_roles()
            ]
            writer.writerow(row)


player_list = []
revalidate = False

if getattr(sys, 'frozen', False):
    file_path = Path(sys.executable)
else:
    file_path = Path(__file__)

file_path = file_path.parent.joinpath('resources')


if "--demo" in argv:
    file_path = file_path.joinpath('_players.csv')
else:
    file_path = file_path.joinpath('players.csv')



if file_path.exists():
    with open(str(file_path), 'r') as file:
        reader = csv.reader(file)
        first_line = True

        for row in reader:

            if first_line or len(row) == 0:
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

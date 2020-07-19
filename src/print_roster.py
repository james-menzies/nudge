from os import path, mkdir
from pathlib import Path

def print_roster(roster):
    title = roster.title
    current_path = Path(__file__)
    root = current_path.parents[1]
    rosters_folder = root.joinpath("rosters")

    if not path.exists(rosters_folder):
        mkdir(rosters_folder)

    file_path = rosters_folder.joinpath(title + ".txt")

    appendix = " ({})"

    counter = 1
    while path.exists(file_path):
        file_path = rosters_folder.joinpath(title + appendix.format(counter) + ".txt")
        counter += 1

    with open(file_path, "w") as file:
        file.write(str(roster))

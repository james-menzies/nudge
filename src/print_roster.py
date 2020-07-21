from os import path, mkdir
from pathlib import Path

def print_roster(roster):
    title = roster.title
    root = Path.home()
    rosters_folder = root.joinpath("StringRosterUtility", "Rosters")
    rosters_folder.mkdir(parents=True, exist_ok=True)

    file_path = rosters_folder.joinpath(title + ".txt")

    appendix = " ({})"

    counter = 1
    while path.exists(file_path):
        file_path = rosters_folder.joinpath(title + appendix.format(counter) + ".txt")
        counter += 1

    with open(file_path, "w") as file:
        file.write(str(roster))

    return file_path.absolute()
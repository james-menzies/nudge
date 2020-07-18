from os import path, mkdir

def print_roster(roster):
    title = roster.title
    if not path.exists("rosters/"):
        mkdir("rosters/")

    file_path = "rosters/" + title + ".txt"
    appendix = " ({})"

    counter = 1
    while path.exists(file_path):
        file_path = "rosters/" + title + appendix.format(counter) + ".txt"
        counter += 1

    with open(file_path, "w") as file:
        file.write(str(roster))

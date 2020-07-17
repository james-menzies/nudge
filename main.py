from display_utils import *
import roster_edit_view
import player_edit_view
import creation_flows
from sys import argv


def edit_players():
    player_edit_view.edit_players()


def create_new_roster():
    roster = creation_flows.create_new_roster()
    roster_edit_view.edit_roster(roster)


def quit_program():
    print("Goodbye!")

welcome = """Welcome to the String Rostering Program.
Please choose from the following options:
"""

options, items = create_option_block("")
items["Edit Player Pool"] = edit_players
items["Create New Roster"] = create_new_roster

if "--demo" in argv:
    welcome = "(Demo Mode Active)\n\n" + welcome

choice_loop(options, start=welcome, end="Exit Program")
print("Goodbye")

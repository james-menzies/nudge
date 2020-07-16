from display_utils import *
import roster_edit_view
import player_edit_view
import roster_creation_flow


def edit_players():
    player_edit_view.edit_players()


def create_new_roster():
    roster = roster_creation_flow.create_new_roster()
    roster_edit_view.edit_roster(roster)


def quit_program():
    print("Goodbye!")


print("Welcome to the String Rostering Program.\n")


options, items = create_option_block("")
items["Edit Player Pool"] = edit_players
items["Create New Roster"] = create_new_roster

choice_loop(options, end="Exit Program")
print("Goodbye")

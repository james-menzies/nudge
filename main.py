from display_utils import choice_loop
import roster_edit_view
import player_edit_view


def edit_players():
    player_edit_view.edit_players()


def create_new_roster():
    roster_edit_view.edit_roster()


def quit_program():
    print("Goodbye!")


print("Welcome to the String Rostering Program.\n")
options = {"Edit Player Pool": edit_players,
           "Create New Roster": create_new_roster}

choice_loop(options, end="Exit Program")
print("Goodbye")

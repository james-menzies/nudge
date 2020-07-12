import display_utils

def edit_players():
    print("editing players")

def create_new_roster():
    print("creating new roster")

def quit_program():
    print("Goodbye!")

print("Welcome to the String Rostering Program.\n")

terminate = False

while not terminate:

    print("Please make a selection.\n")

    options = {"Edit Player Pool": edit_players,
               "Create New Roster": create_new_roster,
               "Exit Program": quit_program}

    user_choice = display_utils.list_selection(list(options.keys()))
    user_choice = options[user_choice]

    if user_choice == quit_program:
        terminate = True

    user_choice()


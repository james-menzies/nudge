from display_utils import create_option_block, choice_loop
from roster_edit_controller import *


def edit_roster(roster):


    options, items = create_option_block("")
    items["Autofill All"] = lambda: handle_auto_populate_all(roster)
    items["Autofill Single Chair"] = lambda: handle_auto_populate(roster)
    items["Remove Player"] = lambda: handle_remove(roster)
    items["Fill/Replace Player"] = lambda: handle_fill(roster)
    items["Swap Players"] = lambda: handle_swap(roster)
    items["Print Roster"] = lambda: handle_print(roster)

    choice_loop(options, refresh_object=roster, end="Go Back to Main:")




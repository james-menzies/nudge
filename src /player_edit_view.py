from display_utils import *
from player_edit_controller import *

def edit_players():

    options, items = create_option_block("")
    items["View Players"] = handle_view
    items["Add a New Player"] = handle_add
    items["Delete Player"] = handle_delete
    items["Edit Player"] = handle_edit
    choice_loop(options, end="Go Back to Main:")
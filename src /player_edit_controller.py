from player import *
from player_DAO import player_list, save
from creation_flows import create_new_player, edit_player
from display_utils import *

continue_str = "Press ENTER to continue>> "

def handle_add():
    clear_screen()
    try:
        player = create_new_player()
        player_list.append(player)
        clear_screen()
        print("Player successfully created.\n")
        save()
        print(get_detailed_player_string(player), end="\n\n")
        input(continue_str)
    except:
        print("Unknown error creating player.")
        input(continue_str)


def handle_view():

    clear_screen()
    if len(player_list) == 0:
        input("There are no players registered, hit ENTER to go back >>")
        return
    player = get_player_from_selection()
    if not player:
        return

    clear_screen()

    print(get_detailed_player_string(player), end="\n\n")
    input(continue_str)


def handle_edit():

    try:
        clear_screen()
        player = get_player_from_selection()
        if not player:
            return
        clear_screen()
        edit_player(player)
        print(f"Player successfully edited\n\n")
        save()
        print(get_detailed_player_string(player))
        input(continue_str)
    except:
        print("Unknown error occurred editing player.")
        input(continue_str)

def handle_delete():

    try:
        clear_screen()
        player = get_player_from_selection()
        if not player:
            return

        confirmation = user_confirmation("""
Are you sure you want to delete this player? (y/n) >> """)
        if confirmation:
            player_list.remove(player)
            print("Player successfully deleted.")
            save()
        else:
            print("Player deletion aborted.")
        input(continue_str)
    except:
        print("Player unable to be removed.")
        input(continue_str)


def get_player_from_selection():
    options, items = create_option_block()
    for player in player_list:
        items[get_player_string(player)] = player

    return list_selection(options, prompt="Select Player:", col_width=40, blank=True)


def get_player_string(player):
    return f"{player.name} ({instruments[player.instrument]})"


def get_detailed_player_string(player):
    return f"""Name: {player.name}
Instrument: {instruments[player.instrument]}
Primary Role: {roles[player.prim_role]}
Secondary Roles: {player.get_sec_roles(view_friendly=True)}
Employment: {employment_types[player.emp]}"""


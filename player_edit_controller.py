from player import *
from player_DAO import player_list, save
from creation_flows import create_new_player, edit_player
from display_utils import *


def handle_add():

    try:
        player = create_new_player()
        player_list.append(player)
        save()
    except:
        print("Unknown error creating player.")


def handle_view():
    player = get_player_from_selection()
    clear_screen()
    print(f"""Name: {player.name}
Instrument: {instruments[player.instrument]}
Primary Role: {roles[player.prim_role]}
Secondary Roles: {player.sec_role}
Employment: {employment_types[player.emp]}
""")
    input("Press ENTER to continue>> ")


def handle_edit():

    try:
        player = get_player_from_selection()
        edit_player(player)
        save()
        print("Player successfully edited. Press ENTER to continue>> ")
    except:
        print("Unknown error occurred editing player.")

def handle_delete():

    try:
        player = get_player_from_selection()
        player_list.remove(player)
        save()
        input("Player successfully deleted. Press ENTER to continue>> ")
    except:
        print("Player unable to be removed.")


def get_player_from_selection():
    options, items = create_option_block()
    for player in player_list:
        items[get_player_string(player)] = player

    return list_selection(options, prompt="Select Player:", col_width=40)


def get_player_string(player):
    return f"{player.name} ({instruments[player.instrument]})"




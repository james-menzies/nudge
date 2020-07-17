from player import instruments
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
    clear_screen()
    string = "Player List \n\n"
    players = ""
    for player in player_list:
        players += get_player_string(player) + "\n"

    players = split_column(players)
    players = render_columns(players, col_width=40)
    string += players
    print(string)
    input("press ENTER to return >> ")


def handle_edit():

    try:
        player = get_player_from_selection()
        edit_player(player)
        save()
        print("Player successfully edited.")
    except:
        print("Unknown error occurred editing player.")

def handle_delete():

    try:
        player = get_player_from_selection()
        del player
        save()
        print("Player successfully deleted.")
    except:
        print("Player unable to be removed.")


def get_player_from_selection():
    options, items = create_option_block()
    for player in player_list:
        items[get_player_string(player)] = player

    return list_selection(options, prompt="Select Player:", col_width=40)


def get_player_string(player):
    return f"{player.name} ({instruments[player.instrument]})"




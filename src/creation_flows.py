from roster import Roster
from display_utils import *
from player import *


def create_new_roster():
    clear_screen()
    name = input("Enter the name of your new program >> ")
    strengths = None
    while not strengths:
        strengths = input("""
Enter your string strengths. For example,
for 8 First Violins, 6 Seconds, 5 Violas, 4 Cellos and 3 Basses,
type "8 6 5 4 3" (max 30 players per section).
>> """)
        strengths = convert_input_to_int(strengths, 1, 30, 5)

    return Roster(strengths, name)


def create_new_player():
    print("Creating new Player\n")
    data = __get_player_data()
    return Player(*data)


def edit_player(player):
    print(f"Editing Player: {player.name}")

    data = __get_player_data(edited_player=player)
    if data[0]:
        player.name = data[0]
    player.instrument = data[1]
    player.prim_role = data[2]
    player.emp = data[3]
    player.sec_role = data[4]


def __get_player_data(edited_player=None):

    if edited_player:
        edit_insert = f", currently {edited_player.name}\n Leave blank if unchanged "
    else:
        edit_insert = " "

    name = input(f"Players Name{edit_insert}>> ")
    clear_screen()

    if edited_player:
        edit_insert = f" (currently {instruments[edited_player.instrument]})"

    instrument = get_enum_from_selection(Instrument,
                                         instruments,
                                         prompt=f"Select Instrument{edit_insert}")

    clear_screen()
    if instrument != Instrument.violin:
        exclusions = [
            Role.principal_2nd,
            Role.concert_master,
            Role.ass_concert_master
        ]
    else:
        exclusions = []

    if edited_player:
        edit_insert = f" (currently {roles[edited_player.prim_role]})"

    prim_role = get_enum_from_selection(Role,
                                        roles,
                                        *exclusions,
                                        prompt=f"Select Primary Role{edit_insert}")

    clear_screen()
    if edited_player:
        edit_insert = f" (currently {employment_types[edited_player.emp]})"
    emp = get_enum_from_selection(Employment,
                                  employment_types,
                                  prompt=f"Select Employment Type {edit_insert}")

    clear_screen()
    exclusions.append(prim_role)

    if edited_player:

        sec_role_insert = []

        for role in edited_player.sec_role:
            sec_role_insert.append(roles[role])
        sec_role_insert = ", ".join(sec_role_insert)

        edit_insert = f" (currently {sec_role_insert})"

    sec_role = get_enum_from_selection(Role,
                                       roles,
                                       *exclusions,
                                       prompt=f"Select Secondary Role, leave blank to skip {edit_insert}",
                                       blank=True)
    clear_screen()
    if sec_role:
        sec_role = [sec_role]
    else:
        sec_role = []
    return [name, instrument, prim_role, emp, sec_role]


def get_enum_from_selection(enum_type, conv, *exclusions, prompt="",blank=False):
    options, items = create_option_block()
    for e in enum_type:
        if e not in exclusions:
            items[conv[e]] = e

    return list_selection(options, prompt=prompt, blank=blank)

from display_utils import *
from roster_operations import *


def handle_swap(roster):

    options, items = create_option_block("")
    for data in Instrument:
        items[data.name] = data

    chosen_inst = list_selection(options, prompt="Select Instrument")
    sections = {}
    for index, section in enumerate(roster.sections):
        if section.instrument == chosen_inst:
            sections[section] = index

    options = []
    for section in sections:

        option, items = create_option_block(section.name)
        items = option['items']
        for index, player in enumerate(section.players):
            items[player.name] = (sections[section], index)
        options.append(option)

    chosen_players = list_selection(*options, multi=2,
                                    prompt="Select 2 players to swap")

    player1, player2 = chosen_players
    roster.swap_players(*player1, *player2)


def handle_auto_populate_all(roster):
    autofill_section(roster)


def handle_auto_populate(roster):
    player_coords = __select_single_player(roster)
    autofill_player(roster, *player_coords)


def handle_print(roster):
    pass


def handle_fill(roster):

    player_coords = __select_single_player(roster)
    replacements = get_player_recommendations(roster, *player_coords)

    options, items = create_option_block("")
    for replacement in replacements:
        user_str = f"{replacement['player'].name} ({replacement['suitability'].value}"
        items[user_str] = replacement['player']

    chosen_replacement = list_selection(options, prompt="Choose Replacement Player")
    roster.replace_player(*player_coords, chosen_replacement)


def handle_remove(roster):
    player_coords = __select_single_player(roster)
    roster.remove_player(*player_coords)


def __select_single_player(roster):
    section_index = __select_child(roster.sections, prompt="Select Section")
    section = roster.sections[section_index]
    chair_index = __select_child(section.players, prompt="Select Player", title=section.name)
    return section_index, chair_index


def __select_child(parent, prompt="", title=""):
    options, items = create_option_block(title)
    for index, child in enumerate(parent):
        items[child.name] = index
    return list_selection(options, prompt=prompt)

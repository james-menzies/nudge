from display_utils import *
from roster_operations import *
from section import suitabilities
from print_roster import print_roster

continue_str = "Press ENTER to continue >> "


def handle_swap(roster):
    clear_screen()
    print("Swap Players")
    options, items = create_option_block("")
    for data in Instrument:
        items[instruments[data]] = data

    chosen_inst = list_selection(options, prompt="Select Instrument")
    clear_screen()
    sections = {}
    for index, section in enumerate(roster.sections):
        if section.instrument == chosen_inst:
            sections[section] = index

    options = []
    for section in sections:

        option, items = create_option_block(section.name)
        items = option['items']
        for index, player in enumerate(section.players):
            ret_value = (sections[section], index)
            if player:
                items[player.name] = ret_value
            else:
                name = f"Vacant Chair ({index + 1})"
                items[name] = ret_value
        options.append(option)

    chosen_players = list_selection(*options, multi=2,
                                    prompt="Select 2 players to swap, type 2 numbers separated by a space.")

    clear_screen()
    player1, player2 = chosen_players
    try:
        viability = roster.check_swap(*player1, *player2)
    except:
        print("An error has occurred. Players not swapped.")
        input(continue_str)
        return
    permission = True
    if Suitability.LessRecommended in viability \
            or Suitability.NonRecommended in viability:
        permission = user_confirmation("""
It appears there are people about to be put in roles outside of their normal duties. 
Would you like to proceed? (y/n) >>""")

    if permission:
        roster.swap_players(*player1, *player2)
        print("Players successfully swapped.")
    else:
        print("Player swap cancelled.")
    input(continue_str)


def handle_auto_populate_all(roster):
    autofill_section(roster)


def handle_auto_populate(roster):
    clear_screen()
    print("Chair Autofill")
    player_coords = __select_single_player(roster)
    autofill_player(roster, *player_coords)


def handle_print(roster):
    clear_screen()
    try:
        file_path = print_roster(roster)
        print(f"{roster.title} roster successfully printed to \n{file_path}")
    except:
        print("An error occurred while printing")
    finally:
        input(continue_str)


def handle_fill(roster):
    clear_screen()
    print("Fill / Replace Player")
    player_coords = __select_single_player(roster)
    replacements = get_player_recommendations(roster, *player_coords)
    if len(replacements) == 0:
        print("There are no suitable players for this position")
        input("Press ENTER to go back >> ")
        return

    options, items = create_option_block("")
    for replacement in replacements:
        user_str = f"{replacement['player'].name} ({suitabilities[replacement['suitability']]})"
        items[user_str] = replacement['player']

    chosen_replacement = list_selection(options, prompt="Choose Player To Fill Chair", col_width=45)
    roster.replace_player(*player_coords, chosen_replacement)

    print(f"Chair filled successfully by {chosen_replacement.name}")
    input(continue_str)


def handle_remove(roster):
    clear_screen()
    print("Remove Player")
    player_coords = __select_single_player(roster)
    player = roster.remove_player(*player_coords)
    confirmation = False
    if player:
        confirmation = user_confirmation("Would you like to make the player unavailable? (y/n) >> ")
    if confirmation:
        player.availability = Availability.unavailable


def __select_single_player(roster):
    section_index = __select_child(roster.sections, prompt="Select Section")
    section = roster.sections[section_index]
    chair_index = __select_child(section.players, prompt="Select Player", title=section.name)
    return section_index, chair_index


def __select_child(parent, prompt="", title=""):
    options, items = create_option_block(title)
    for index, child in enumerate(parent):
        if child:
            items[child.name] = index
        else:
            name = f"Vacant Chair ({index + 1})"
            items[name] = index
    return list_selection(options, prompt=prompt)


def reset_roster(roster):
    for player in player_list:
        player.availability = Availability.reserve

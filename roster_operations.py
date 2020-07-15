from player_DAO import player_list
from roster import *
import random


def get_player_recommendations(roster, sect_ind, chair_ind, threshold=Suitability.Illegal):

    def sort_recommendations(list):
        return list["suitability"].value

    recommendations = []
    players = random.sample(player_list, len(player_list))

    for player in players:
        suitability = roster.check_chair(sect_ind, chair_ind, player)
        correct_instrument = suitability.value < threshold.value
        available = player.availability == Availability.reserve
        if correct_instrument and available:
            recommendations.append({
                "player": player,
                "suitability": suitability
            })

    recommendations.sort(key=sort_recommendations)
    return recommendations


def autofill_player(roster, section_ind, chair_ind, threshold=Suitability.NonPrimary):

    recs = get_player_recommendations(roster, section_ind, chair_ind, threshold)
    if len(recs):
        result = roster.replace_player(section_ind, chair_ind, recs[0]["player"])
        if result:
            return result
        else:
            return True
    else:
        return False


def autofill_section(roster):

    complete = __autofill_pass(roster)
    if not complete:
        __autofill_pass(roster, Suitability.Casual)


def __autofill_pass(roster, threshold=Suitability.NonPrimary):
    complete = True

    for section_ind, section in enumerate(roster.sections):
        for chair_ind, player in enumerate(section.players):
            if not player:
                success = autofill_player(roster, section_ind, chair_ind, threshold)
                complete = success and complete

    return complete

from section import Section, Suitability
from player import *
from display_utils import render_columns


class Roster:

    def __init__(self, section_sizes, title="Untitled Program"):

        sizes = iter(section_sizes)
        try:
            violin_1 = Section("Violin 1", Instrument.violin, next(sizes))
            violin_2 = Section("Violin 2", Instrument.violin, next(sizes))
            viola = Section("Violas", Instrument.viola, next(sizes))
            cello = Section("Cellos", Instrument.cello, next(sizes))
            double_basses = Section("Double Basses", Instrument.double_bass, next(sizes))
        except IndexError:
            raise ValueError("Error creating roster, make sure section sizes contains 5 integers")

        self.title = title
        self.__sections = [violin_1, violin_2, viola, cello, double_basses]
        for section in self.__sections:
            section.add_role(0, Role.principal)

        violin_1.add_role(0, Role.concert_master)
        violin_1.add_role(1, Role.ass_concert_master)
        violin_1.add_role(2, Role.principal)
        violin_2.add_role(0, Role.principal_2nd)

    @property
    def sections(self):
        return tuple(self.__sections)

    def __repr__(self):
        result = self.title + "\n\n"
        result += render_columns(self.__sections[:])
        return result

    def replace_player(self, sect_ind, chair_ind, player):

        old_player = self.remove_player(sect_ind, chair_ind)

        section = self.__sections[sect_ind]
        try:
            section.seat_player(chair_ind, player)
            return old_player
        except ValueError as error:
            if old_player:
                section.seat_player(chair_ind, old_player)
            return error

    def remove_player(self, sect_ind, chair_ind):
        return self.__sections[sect_ind].remove_player(chair_ind)

    def check_chair(self, sect_ind, chair_ind, player):
        return self.__sections[sect_ind].check_chair(chair_ind, player)

    def check_swap(self, section_a, chair_a, section_b, chair_b):

        suitability = []

        player_a = self.sections[section_a].players[chair_a]
        player_b = self.sections[section_b].players[chair_b]

        case_a = self.sections[section_b].check_chair(chair_b, player_a)
        case_b = self.sections[section_a].check_chair(chair_a, player_b)

        suitability.append(case_a)
        suitability.append(case_b)
        return tuple(suitability)

    def swap_players(self, section_a, chair_a, section_b, chair_b):
        suitability = self.check_swap(section_a, chair_b, section_b, chair_b)
        if Suitability.Illegal in suitability:
            raise ValueError("An illegal swap operation was attempted in roster")

        player_a = self.remove_player(section_a, chair_a)
        player_b = self.remove_player(section_b, chair_b)

        self.replace_player(section_b, chair_b, player_a)
        self.replace_player(section_a, chair_a, player_b)

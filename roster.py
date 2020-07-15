from section import Section, Suitability
from player import *


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
        repr = self.title + "\n\n"
        repr += self.__repr_section_cluster(self.__sections[0:3])
        repr += self.__repr_section_cluster(self.__sections[3:])
        return repr

    def __repr_section_cluster(self, sections):

        max_rows = 0

        cluster = ""

        for index, section in enumerate(sections):
            section = str(section)
            section = section.split(sep="\n")
            sections[index] = section
            if len(section) > max_rows:
                max_rows = len(section)

        for i in range(0, max_rows):
            for section in sections:
                if i >= len(section):
                    name_str = ""
                else:
                    name_str = section[i]

                cluster += "{0:30}".format(name_str)
            cluster += "\n"

        return cluster

    def seat_player(self, sect_ind, seat_ind, player):
        section = self.__sections[sect_ind]
        try:
            section.seat_player(seat_ind, player)
        except ValueError as error:
            return error

    def remove_player(self, sect_ind, seat_ind):
        return self.__sections[sect_ind].remove_player(seat_ind)

    def check_swap(self, section_a, seat_a, section_b, seat_b):

        suitability = []

        player_a = self.sections[section_a].players[seat_a]
        player_b = self.sections[section_b].players[seat_b]

        case_a = self.sections[section_b].check_chair(seat_b, player_a)
        case_b = self.sections[section_a].check_chair(seat_a, player_b)

        suitability.append(case_a)
        suitability.append(case_b)
        return tuple(suitability)

    def swap_players(self, section_a, seat_a, section_b, seat_b):
        suitability = self.check_swap(section_a, seat_b, section_b, seat_b)
        if Suitability.Illegal in suitability:
            raise ValueError("An illegal swap operation was attempted in roster")

        player_a = self.remove_player(section_a, seat_b)
        player_b = self.remove_player(section_b, seat_b)

        self.seat_player(section_b, seat_b, player_a)
        self.seat_player(section_a, seat_a, player_b)

from section import Section
from player import Instrument
from player import Role


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

    @property
    def sections(self):
        return tuple(self.__sections)

    def __repr__(self):
        repr = self.title + "\n"
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



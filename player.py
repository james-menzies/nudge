import enum
from model_utils import check_type

player_init_error = "Wrong data type submitted in player init"
violin_init_error = "Attempted to assign violin role to non violinist"


class Player:
    def __init__(self, name, instrument, prim_role, emp, sec_role=[]):
        self.name = name
        self.instrument = check_type(instrument, Instrument)
        self.prim_role = check_type(prim_role, Role)
        self.emp = check_type(emp, Employment)
        self.sec_role = check_type(sec_role, Role)
        self.availability = Availability.reserve

        # check for invalid violin-only attr
        def assert_non_violin(role):
            if role.value < 3:
                raise ValueError(violin_init_error)

        if instrument != Instrument.violin:
            assert_non_violin(prim_role)
            for role in sec_role:
                assert_non_violin(role)

    def __repr__(self):
        return f"Name: {self.name}, Instrument: {self.instrument.name}, " \
               f"Role: {self.prim_role.name}, Employment: {self.emp.name} " \
               f"Other Roles: {self.sec_role}, Availability: {self.availability.name}"


class Role(enum.Enum):
    concert_master = 0
    ass_concert_master = 1
    principal_2nd = 2
    principal = 3
    tutti = 4


def get_roster_symbol(role):
    if role == Role.concert_master:
        return "(C.M.)"
    elif role == Role.ass_concert_master:
        return "(A.C.M.)"
    else:
        return ""


class Instrument(enum.Enum):
    violin = 0
    viola = 1
    cello = 2
    double_bass = 3


class Employment(enum.Enum):
    permanent = 0
    casual = 1


class Availability(enum.Enum):
    engaged = 0
    reserve = 1
    unavailable = 2

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
        self.sec_role = tuple(check_type(sec_role, Role))
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
        return f"Name: {self.name}, Instrument: {instruments[self.instrument]}, " \
               f"Role: {roles[self.prim_role]}, Employment: {employment_types[self.emp]} " \
               f"Other Roles: {self.sec_role}, Availability: {self.availability.name}"

    def performs_role(self, role):
        prim = role == self.prim_role
        sec = role in self.sec_role

        return prim or sec

    def get_sec_roles(self, view_friendly=False):
        sec_role_str = []
        for role in self.sec_role:
            if view_friendly:
                role_str = roles[role]
            else:
                role_str = role.name
            sec_role_str.append(role_str)
        return ",".join(sec_role_str)


class Role(enum.Enum):
    concert_master = 0
    ass_concert_master = 1
    principal_2nd = 2
    principal = 3
    tutti = 4


roles = {
    Role.concert_master: "Concert Master",
    Role.ass_concert_master: "Associate Concert Master",
    Role.principal_2nd: "Principal 2nd Violin",
    Role.principal: "Principal",
    Role.tutti: "Tutti"
}


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

    def __repr__(self):
        if self == Instrument.violin:
            return "Violin"
        elif self == Instrument.viola:
            return "Viola"
        elif self == Instrument.cello:
            return "Cello"
        else:
            return "Double Bass"


instruments = {
    Instrument.violin: "Violin",
    Instrument.viola: "Viola",
    Instrument.cello: "Cello",
    Instrument.double_bass: "Double Bass"

}


class Employment(enum.Enum):
    permanent = 0
    casual = 1


employment_types = {
    Employment.permanent: "Permanent",
    Employment.casual: "Casual"
}

class Availability(enum.Enum):
    engaged = 0
    reserve = 1
    unavailable = 2

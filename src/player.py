import enum
from model_utils import check_type

player_init_error = "Wrong data type submitted in player init"
violin_init_error = "Attempted to assign violin role to non violinist"


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


class Player:
    def __init__(self, name, instrument, prim_role, emp, sec_role=[]):
        self.name = name
        self.prim_role = prim_role
        self.sec_role = sec_role
        self.emp = emp
        self.instrument = instrument
        self.availability = Availability.reserve

    def __repr__(self):
        return f"Name: {self.name}, Instrument: {instruments[self.instrument]}, " \
               f"Role: {roles[self.prim_role]}, Employment: {employment_types[self.emp]} " \
               f"Other Roles: {self.sec_role}, Availability: {self.availability.name}"

    def __plays_violin_role(self):
        if self.prim_role.value < 3:
            return True

        for role in self.sec_role:
            if role.value < 3:
                return True

        return False

    @property
    def instrument(self):
        return self._instrument

    @instrument.setter
    def instrument(self, value):
        check_type(value, Instrument)
        if value != Instrument.violin and self.__plays_violin_role():
            raise ValueError("Non-violinist cannot hold violin-only role")
        self._instrument = value

    @property
    def prim_role(self):
        return self._prim_role

    @prim_role.setter
    def prim_role(self, value):
        check_type(value, Role)
        self._prim_role = value

    @property
    def sec_role(self):
        return tuple(self._sec_role)

    @sec_role.setter
    def sec_role(self, value):
        check_type(value, Role)
        self._sec_role = value

    @property
    def emp(self):
        return self._emp

    @emp.setter
    def emp(self, value):
        check_type(value, Employment)
        self._emp = value

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        check_type(value, Availability)
        self._availability = value

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


def get_roster_symbol(role):
    if role == Role.concert_master:
        return "(C.M.)"
    elif role == Role.ass_concert_master:
        return "(A.C.M.)"
    else:
        return ""

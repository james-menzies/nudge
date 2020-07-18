from player import *
import enum

default_refresh = lambda pos, player: None


class Section:
    def __init__(self, name, instrument, size):
        self.name = name
        self.__instrument = check_type(instrument, Instrument)
        check_type(size, int)

        self.__players = []
        for i in range(0, size):
            self.__players.append(None)

        self.__roles = {}

    @property
    def instrument(self):
        return self.__instrument

    @property
    def players(self):
        return tuple(self.__players)

    def add_role(self, pos, role):
        check_type(role, Role)
        check_type(pos, int)
        self.__roles[pos] = role

    def check_chair(self, pos, player):
        if not player:
            return Suitability.OK

        role = self.get_role(pos)
        if player.instrument != self.__instrument:
            return Suitability.Illegal
        elif player.emp == Employment.permanent:
            return self.__check_permanent(role, player)
        else:
            return self.__check_casual(role, player)

    def get_role(self, pos):
        if pos in self.__roles:
            return self.__roles[pos]
        else:
            return Role.tutti

    def remove_player(self, pos):
        old_player = self.__players[pos]
        self.__players[pos] = None

        if old_player:
            old_player.availability = Availability.reserve
        return old_player

    def seat_player(self, pos, player):

        check_type(player, Player)

        if player.instrument == self.__instrument:
            old_player = self.__players[pos]
            self.__players[pos] = player

            if old_player:
                old_player.availability = Availability.reserve
            player.availability = Availability.engaged

            return old_player
        else:
            raise ValueError("Attempted to place wrong instrumentalist in section.")

    def __check_permanent(self, role, player):

        if player.prim_role == role:
            return Suitability.OK
        elif role in player.sec_role:
            return Suitability.NonPrimary
        else:
            return Suitability.LessRecommended

    def __check_casual(self, role, player):

        if player.prim_role == role:
            return Suitability.Casual
        if role in player.sec_role:
            return Suitability.LessRecommended
        else:
            return Suitability.NonRecommended

    def __repr__(self):
        repr = f"{self.name}\n"
        for pos, player in enumerate(self.__players):
            if pos % 2 == 0:
                repr += "\n"
            repr += self.__player_repr(pos, player) + "\n"

        return repr

    def __player_repr(self, pos, player):
        role = self.get_role(pos)
        casual = player and player.emp == Employment.casual
        promoted = player and player.prim_role.value > role.value

        if role == Role.tutti and casual:
            prefix = "~"
        elif role == Role.tutti:
            prefix = " "
        elif not player:
            prefix = "*"
        elif casual:
            prefix = "#"
        elif promoted:
            prefix = "#"
        else:
            prefix = "*"

        if player:
            name = player.name
        else:
            name = "Chair Vacant"

        suffix = get_roster_symbol(role)
        return f"{prefix} {name} {suffix}"


class Suitability(enum.Enum):
    # Primary Role Permanent
    OK = 0
    # Sec Role Permanent
    NonPrimary = 1
    # Primary Casual
    Casual = 2
    # S Casual/Non Sec Permanent
    LessRecommended = 3
    # Non Sec Casual
    NonRecommended = 4
    # Wrong Instrument
    Illegal = 5

suitabilities = {

    Suitability.OK: "Reg.",
    Suitability.NonPrimary: "Sec.",
    Suitability.Casual: "Cas.",
    Suitability.LessRecommended: "L.R.",
    Suitability.NonRecommended: "N.R.",
    Suitability.Illegal: "N/A"
}
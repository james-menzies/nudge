from player import *
import enum
default_refresh = lambda pos, player: None

class Section:
    def __init__(self, name, instrument, size, refresh=default_refresh):
        self.name = name
        self.__instrument = check_type(instrument, Instrument)
        check_type(size, int)

        self.__players = []
        for i in range(0, size):
            self.__players.append(None)

        self.__roles = {}
        self.__refresh = refresh


    @property
    def instrument(self):
        return self.__instrument

    @instrument.setter
    def instrument(self, value):
        if check_type(value, Instrument):
            self.__instrument = value

    def add_role(self, pos, role):
        check_type(role, Role)
        check_type(pos, int)
        self.__roles[pos] = role

    def check_chair(self, pos, player):
        role = None
        if pos in self.__roles:
            role = self.__roles[pos]
        else:
            role = Role.tutti

        if player.instrument != self.__instrument:
            return Suitability.Illegal
        elif player.emp == Employment.permanent:
            return self.__check_permanent(role, player)
        else:
            return self.__check_casual(role, player)

    def seat_player(self, pos, player):

        check_type(player, Player)

        if player.instrument == self.__instrument:
            old_player = self.__players[pos]
            self.__players[pos] = player
            self.__refresh(pos, player)
            return old_player
        else:
            raise ValueError("Attempted to place wrong instrumentalist in section.")



    def __check_permanent(self, role, player):

        if player.prim_role == role:
            return Suitability.OK
        elif role in player.sec_role:
            return Suitability.NonPrimary
        else:
            return Suitability.NonRecommended


    def __check_casual(self, role, player):

        if player.prim_role == role:
            return Suitability.Casual
        if role in player.sec_role:
            return Suitability.LessRecommended
        else:
            return Suitability.NonRecommended

    def __repr__(self):
        repr = f"{self.name}\n\n"
        for player in self.__players:
            repr += player.name


class Suitability(enum.Enum):

    # Primary Role Permanent
    OK: 0
    # Sec Role Permanent
    NonPrimary: 1
    # Primary Casual
    Casual: 2
    # S Casual/Non Sec Permanent
    LessRecommended: 3
    # Non Sec Casual
    NonRecommended: 4
    # Wrong Instrument
    Illegal: 5





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
    def players(self):
        return tuple(self.__players)

    def add_role(self, pos, role):
        check_type(role, Role)
        check_type(pos, int)
        self.__roles[pos] = role

    def check_chair(self, pos, player):
        role = self.__get_role(pos)
        if player.instrument != self.__instrument:
            return Suitability.Illegal
        elif player.emp == Employment.permanent:
            return self.__check_permanent(role, player)
        else:
            return self.__check_casual(role, player)

    def __get_role(self, pos):
        if pos in self.__roles:
            return self.__roles[pos]
        else:
            return Role.tutti

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
        for index, player in enumerate(self.__players):

            role = self.__get_role(index)
            casual = player and player.emp == Employment.casual
            promoted = player and player.prim_role.value > role.value

            prefix = None
            if role == Role.tutti:
                prefix = ""
            elif not player:
                prefix = "*"
            elif casual:
                prefix = "#"
            elif promoted:
                prefix = "#"
            else:
                prefix = "*"

            name = None
            if player:
                name = player.name
            else:
                name = "Chair Vacant"

            suffix = get_roster_symbol(role)
            repr += f"{prefix} {name} {suffix}\n"
        return repr

            # if player:
            #     role = self.__get_role(index)
            #
            #     promoted = player.prim_role.value > self.__get_role(index).value
            #
            #     if casual or promoted:
            #         repr += "# "
            #     elif role != Role.tutti:
            #         repr += "* "
            #     repr += player.name
            #
            #
            # else:
            #     repr += "Chair Vacant"
            #
            # appendix = get_roster_symbol(self.__get_role(index))
            # repr += f"  {appendix}\n"
        return repr


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

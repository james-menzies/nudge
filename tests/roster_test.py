from roster import Roster
from player_DAO import player_list
from os import system
roster = Roster([16, 14, 12, 10, 8], title="Masters Series 1")

roster.sections[0].seat_player(0, player_list[0])
print(roster)
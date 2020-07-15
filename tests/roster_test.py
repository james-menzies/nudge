from roster import Roster
from player_DAO import player_list

roster = Roster([10, 6, 5, 4, 3], title="Masters Series 1 (24th June, 1969)")
roster.replace_player(0, 0, player_list[0])
print(roster)
print(roster.check_swap(0, 0, 2, 0))
print(roster.swap_players(0, 0, 2, 0))
print(roster)


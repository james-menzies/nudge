from section import Section
from player import *
from player_DAO import player_list

section = Section("Violin 1", Instrument.violin, 8)
section.add_role(0, Role.concert_master)
section.add_role(1, Role.ass_concert_master)
section.add_role(2, Role.principal)

section.seat_player(6, player_list[2])
section.seat_player(4, player_list[11])
section.seat_player(2, player_list[62])
print(section)


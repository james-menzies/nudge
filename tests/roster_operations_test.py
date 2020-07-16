from roster import *
from roster_operations import *

roster = Roster([10, 8, 6, 6, 4], title="Untitled Princess Caroline Project")




autofill_section(roster)

print(roster)

roster.swap_players(0,9,1,7)

print(roster)
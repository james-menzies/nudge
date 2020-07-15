from roster import *
from roster_operations import *

roster = Roster([16, 14, 12, 10, 8], title="Untitled Princess Caroline Project")

# recs = get_player_recommendations(roster, 0, 0)
# for rec in recs:
#     name = rec['player'].name
#     suit = rec['suitability']
#     print(f"{name}, {suit}")


autofill_section(roster)

print(roster)
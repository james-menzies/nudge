from roster_edit_controller import *
from roster import *
import roster_operations

roster = Roster([8, 6, 5, 4, 3])
roster_operations.autofill_section(roster)

print(roster)
handle_fill(roster)

print(roster)
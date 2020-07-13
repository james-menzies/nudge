from player import *

james = Player("James Menzies", Instrument.violin, Role.tutti, Employment.permanent, sec_role=[Role.ass_concert_master])

print (james.name, james.prim_role.name, james.emp.name)
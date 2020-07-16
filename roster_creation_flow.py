from roster import Roster
from display_utils import convert_input_to_int, clear_screen

def create_new_roster():
    clear_screen()
    name = input("Enter the name of your new program>> ")
    strengths = None
    while not strengths:
        strengths = input("""
Enter your string strenths. For example,
for 8 First Violins, 6 Seconds, 5 Violas, 4 Cellos and 3 Basses,
type "8 6 5 4 3" (max 30 players per section).
>> """)
        strengths = convert_input_to_int(strengths, 1, 30, 5)

    return Roster(strengths, name)

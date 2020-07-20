def show_help():
    pass


navigation_text = """
General Navigation
------------------

Most of the application is traversed through list selection which done
consistently through entering numbers into the terminal. The input is always
tested and handled for validity to ensure the program will continue properly
regardless of the actual input. In fact, the only actual typing required by 
the user is when typing a name when editing a player. If you need to type more
than one number, simply type the numbers followed by a space. For example,
when trying to swap 2 players, type "2 5" to swap the second and fifth player.

There are 2 main parts to the application; where the user can manage the 
player database and roster creation. Both of these are accessed from the main 
menu.
"""

player_text = """
Player Management
-----------------

There are four operations that can be performed here. If the user wishes to 
cancel any action mid-operation, all they need do is press ENTER whilst 
leaving the input blank.

VIEW: Upon selecting this option the user will be presented with the names of 
all the stored players with their instrument. Upon selecting a player, more 
detailed info about that person will be displayed.

ADD: This will take the user through the player creation flow, and upon 
completion, the new player will be added to the player bank. This flow can be 
canceled safely at any point.

DELETE: This will remove the player. The user will be asked to confirm the action.

EDIT: The user will be taken through the same creation flow as when adding a 
player, except the user will be informed of any previous attributes. It is important
to note here that hitting ENTER on name selection will indicate to the program that
the same name is to be kept, so the action will not be terminated.
"""

roster_text = """
Roster Editing
--------------

The user will be taken through an initial creation flow where the name and 
size of each section will be set. From there, there are 6 available operations:

AUTOFILL ALL: Each chair will attempt to be filled via the autofill function. Only primary and secondary permanent candidates will be chosen.

AUTOFILL CHAIR: As above but with a single chair.

REMOVE PLAYER: Will remove a seated player. The user has the option to 
designate the player as unavailable making them ineligible for future selection.

FILL / REPLACE PLAYER: Upon selecting a chair the user will be given a list of 
recommendations of candidates. This will remove a player is one is already 
present in the chair.

SWAP PLAYERS: This will allow two players of the same section to be swapped by 
typing in two ordinal numbers. A warning will be displayed if the swap 
involves players performing outside of their usual role.

PRINT: This will export the roster in its current state to the Rosters folder. 
The roster will be stored in plain text.
"""

from display_utils import *

def show_help():
    options, items = create_option_block()
    items["General Navigation"] = lambda: __show_segment(navigation_text)
    items["Player Management"] = lambda: __show_segment(player_text)
    items["Roster Management"] = lambda: __show_segment(roster_text)
    choice_loop(options, start="Select a Topic You Would Like Help On")

def __show_segment(text_block):
    clear_screen()
    print(text_block)
    input("Press ENTER to go back >> ")

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

This is where you can maintain your database of players. There are four options
available here:

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
the same name is to be kept, rather than to cancel the player edit.
"""

roster_text = """
Roster Editing
--------------

This is where you can create rosters for your programs. When you select this option,
you will be guided through a prompt to set up a name and string strength for your program.
From there, the following six actions are available to you.

AUTOFILL ALL: Each chair will attempt to be filled via the autofill function. Only primary 
and secondary permanent candidates will be chosen.

AUTOFILL CHAIR: As above but with a single chair.

REMOVE PLAYER: Will remove a seated player. The user has the option to 
designate the player as unavailable which will make them ineligible for future
 selection.

FILL / REPLACE PLAYER: Upon selecting a chair the user will be given a list of 
recommendations of candidates. If targeting a chair that already has a player seated,
they will be removed.

SWAP PLAYERS: This will allow two players of the same section to be swapped by 
typing in two ordinal numbers. A warning will be displayed if the swap 
involves players performing outside of their usual role.

PRINT: This will export the roster in its current state to the StringRosters folder. 
The rosters folder is located in your home directory, and the roster will be stored
as a plain text file.
"""

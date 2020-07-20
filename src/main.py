#!/usr/bin/env python3

from display_utils import *
from help import show_help
import roster_edit_view
import player_edit_view
import creation_flows
from os import system
import sys

def display_help():
    show_help()

def edit_players():
    player_edit_view.edit_players()


def create_new_roster():
    roster = creation_flows.create_new_roster()
    roster_edit_view.edit_roster(roster)


def quit_program():
    print("Goodbye!")

def size_window():
    system('mode con: cols=180 lines=55')


size_window()

welcome = """Welcome to the String Rostering Program.
Please choose from the following options:
"""

options, items = create_option_block("")
items["Edit Player Pool"] = edit_players
items["Create New Roster"] = create_new_roster
items["View Help"] = display_help

if "--demo" in sys.argv:
    welcome = "(Demo Mode Active)\n\n" + welcome

choice_loop(options, start=welcome, end="Exit Program")
print("Goodbye")

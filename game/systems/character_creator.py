import curses
from UI.character_creation_screen import character_creation_screen
from modules.player_module import Player


def create_player_character(stdscr):
    name = character_creation_screen(stdscr)

    return name


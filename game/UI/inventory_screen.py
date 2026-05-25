import curses
from player_module import Player

def open_inventory_window(stdscr, player):
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    inventory_window = curses.newwin(20, 20, int(stdscr_y // 2), int(stdscr_x // 2))
    inventory_window.box()
    inventory = player.inventory

    inventory_window.addstr(1, 1, f"{inventory}")

    inventory_window.refresh()
    inventory_window.getch()


import curses
from player_module import Player

def open_inventory_window(stdscr, player):

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        # inventory_height = max(10, int(stdscr_y * 0.04))
        # inventory_width = max(20, int(stdscr_x * 0.04))
        # start_y = int(stdscr_y * 0.3)
        # start_x = int(stdscr_x * 0.3)
        margin_y = int(stdscr_y * 0.3)
        margin_x = int(stdscr_x * 0.3)
        height = stdscr_y - (margin_y * 2)
        width = stdscr_x - (margin_x * 2)
        inventory_window = curses.newwin(height, width, margin_y, margin_x)
        inventory_window.box()
        inventory = player.inventory

        inventory_window.addstr(1, (int(width / 2) - 11), f"Inventory ({len(inventory)})")
        inventory_window.addstr(2, 1, str(inventory)[:width - 2])

        inventory_window.refresh()
        key = stdscr.getch()

        if key in (ord("i"), ord("I"), 27):
            # inventory_window.erase()
            # inventory_window.refresh()
            stdscr.clear()
            stdscr.refresh()
            break

        if key == curses.KEY_RESIZE:
            curses.resize_term(0, 0)
            stdscr.clear()
            continue

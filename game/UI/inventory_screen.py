import curses
from player_module import Player

def open_inventory_window(stdscr, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_item = None

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        margin_y = int(stdscr_y * 0.3)
        margin_x = int(stdscr_x * 0.3)
        height = stdscr_y - (margin_y * 2)
        width = stdscr_x - (margin_x * 2)
        inventory_window = curses.newwin(height, width, margin_y, margin_x)
        inventory_window.box()
        inventory = player.inventory

        inventory_window.addstr(1, (int(width / 2) - 11), f"Inventory ({len(inventory)})")
        inventory_window.addstr(2, 1, str(inventory)[:width - 2])

        item_rows = {}

        for index, item in enumerate(inventory):
            row = 3 + index

            inventory_window.addstr(row, 2, item["name"])

            item_rows[margin_y + row] = item

        if selected_item:
            detail_x = width // 2

            inventory_window.addstr(3, detail_x, selected_item["name"])
            inventory_window.addstr(4, detail_x, f"{selected_item.get('min_dmg', 0)} - {selected_item.get('max_dmg', 0)}")
            inventory_window.addstr(5, detail_x, f"HP: + {selected_item.get('hp', 0)}")
            inventory_window.addstr(6, detail_x, f"STR: + {selected_item.get('st', 0)}")
            inventory_window.addstr(7, detail_x, f"DEF: + {selected_item.get('df', 0)}")

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

        if key == curses.KEY_MOUSE:
            _, mouse_x, mouse_y, _, button_state = curses.getmouse()

            if button_state and curses.BUTTON1_CLICKED:
                if mouse_y in item_rows:
                    selected_item = item_rows[mouse_y]

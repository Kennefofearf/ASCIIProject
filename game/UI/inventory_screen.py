import curses
from player_module import Player
from data.affix_data import UNCOMMON_AFFIXES

def open_inventory_window(stdscr, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_item = None

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        margin_y = int(stdscr_y * 0.3)
        margin_x = int(stdscr_x * 0.3)
        height = stdscr_y - (margin_y * 2)
        width = stdscr_x - (margin_x * 2)

        dw_margin_y = int(stdscr_y * 0.3)
        dw_margin_x = int(stdscr_x * 0.6)
        inventory_window = curses.newwin(height, width, margin_y, margin_x)
        inventory_window.box()
        inventory = player.inventory

        inventory_window.addstr(1, (int(width / 2) - 11), f"Inventory ({len(inventory)})")
        #inventory_window.addstr(2, 1, str(inventory)[:width - 2])

        item_rows = {}

        for index, item in enumerate(inventory):
            row = 3 + index

            inventory_window.addstr(row, 2, item["name"])

            item_rows[margin_y + row] = item

        if selected_item:

            item_description_window = curses.newwin(height, width, dw_margin_y, dw_margin_x)
            item_description_window.box()

            detail_x = width // 2

            affixes = selected_item.get("affixes", [])

            row = 5

            for affix_id in affixes:
                affix_data = UNCOMMON_AFFIXES[affix_id]

                item_description_window.addstr(row, detail_x, selected_item["name"])
                row += 1
                item_description_window.addstr(row, detail_x, f"{selected_item['min_dmg'] + affix_data['min_dmg']}"
                                                       f" - {selected_item['max_dmg'] + affix_data['max_dmg']}")
                row += 1

                affix_stats = affix_data.get("affix_stats", {})

                for stat, value in affix_stats.items():
                    item_description_window.addstr(row, detail_x, f"{stat.upper()}: {value}")
                    row += 1
                item_description_window.refresh()

            if not affixes:
                item_description_window.addstr(row, detail_x, selected_item["name"])
                row += 1
                item_description_window.addstr(row, detail_x, f"{selected_item['min_dmg']} - {selected_item['max_dmg']}")
                item_description_window.refresh()

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

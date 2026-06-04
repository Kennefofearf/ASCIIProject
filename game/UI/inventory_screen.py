import curses
from player_module import Player
from data.affix_data import UNCOMMON_AFFIXES
from systems.loot_generator import get_rarity_color

def open_inventory_window(stdscr, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_item = None
    item_description_window = None

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        inventory_width = int(stdscr_x * 0.35)
        description_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        inventory_x = int(stdscr_x * 0.10)
        description_x = int(stdscr_x * 0.55)

        inventory_window = curses.newwin(height, inventory_width, start_y, inventory_x)
        inventory_window.box()
        inventory = player.inventory

        inventory_window.addstr(1, (int(inventory_width / 2) - 11), f"Inventory ({len(inventory)})")

        item_rows = {}

        for index, item in enumerate(inventory):

            display_name = item["name"]

            if item == player.weapon:
                display_name = "* " + display_name

            item_color = get_rarity_color(item)
            row = 3 + index

            inventory_window.addstr(row, 2, display_name, curses.color_pair(item_color))

            item_rows[start_y + row] = item

        if selected_item:

            item_color = get_rarity_color(selected_item)
            item_description_window = curses.newwin(height, description_width, start_y, description_x)
            item_description_window.box()

            detail_x = description_width // 9

            affixes = selected_item.get("affixes", [])

            row = 5

            for affix_id in affixes:
                affix_data = UNCOMMON_AFFIXES[affix_id]

                predicted_stat_change_hp = (player.max_hp + selected_item.get('base_stats', {}).get('max_hp')
                                                        + affix_data.get('affix_stats', {}).get('max_hp')) - player.max_hp

                predicted_stat_change_st = (player.st + selected_item.get('base_stats', {}).get('st')
                                                        + affix_data.get('affix_stats', {}).get('st')) - player.st

                predicted_stat_change_df = (player.df + selected_item.get('base_stats', {}).get('df')
                                                        + affix_data.get('affix_stats', {}).get('df')) - player.df

                if player.weapon == selected_item:
                    stat_forecast_hp = player.max_hp
                    stat_forecast_st = player.st
                    stat_forecast_df = player.df
                else:
                    stat_forecast_hp = player.max_hp + predicted_stat_change_hp
                    stat_forecast_st = player.st + predicted_stat_change_st
                    stat_forecast_df = player.df + predicted_stat_change_df


                item_description_window.addstr(row, detail_x, selected_item["name"], curses.color_pair(item_color))
                row += 1
                item_description_window.addstr(row, detail_x, f"{selected_item['min_dmg'] + affix_data['min_dmg']}"
                                                       f" - {selected_item['max_dmg'] + affix_data['max_dmg']}")
                row += 1

                affix_stats = affix_data.get("affix_stats", {})

                for stat, value in affix_stats.items():
                    item_description_window.addstr(row, detail_x, f"{stat.upper()}: {value}")
                    row += 1

                row += 5

                item_description_window.addstr(row, detail_x,
                                               f" HP: {player.max_hp} --> {stat_forecast_hp}")
                row += 1
                item_description_window.addstr(row, detail_x,
                                               f"STR: {player.st} --> {stat_forecast_st}")
                row += 1
                item_description_window.addstr(row, detail_x,
                                               f"DEF: {player.df} --> {stat_forecast_df}")

                row += 3
                item_description_window.addstr(row, detail_x, f"(E)quip")
                row += 1
                item_description_window.addstr(row, detail_x, f"(R)emove")

                if key == ord("e"):

                    if player.weapon:
                        player.weapon = None

                    player.weapon = selected_item
                    item_description_window.erase()
                    item_description_window.refresh()
                    selected_item = None
                    continue
                elif key == ord("r"):
                    player.weapon = None
                    item_description_window.erase()
                    item_description_window.refresh()
                    selected_item = None
                    continue

                item_description_window.refresh()

            if not affixes:

                if player.weapon:
                    stat_forecast_hp = player.max_hp + affix_data.get('base_stats', {}).get('max_hp')
                    stat_forecast_st = player.st + affix_data.get('base_stats', {}).get('st')
                    stat_forecast_df = player.df + affix_data.get('base_stats', {}).get('df')
                else:
                    stat_forecast_hp = player.max_hp
                    stat_forecast_st = player.st
                    stat_forecast_df = player.df


                item_description_window.addstr(row, detail_x, selected_item["name"])
                row += 1
                item_description_window.addstr(row, detail_x, f"{selected_item['min_dmg']} - {selected_item['max_dmg']}")
                row += 5

                item_description_window.addstr(row, detail_x,
                                               f" HP: {player.max_hp} --> {stat_forecast_hp}")
                row += 1
                item_description_window.addstr(row, detail_x,
                                               f"STR: {player.st} --> {stat_forecast_st}")
                row += 1
                item_description_window.addstr(row, detail_x,
                                               f"DEF: {player.df} --> {stat_forecast_df}")
                row += 3
                item_description_window.addstr(row, detail_x, f"(E)quip")
                row += 1
                item_description_window.addstr(row, detail_x, f"(R)emove")

                item_description_window.refresh()

                if key == ord("e"):

                    if player.weapon:
                        player.weapon = None

                    player.weapon = selected_item
                    item_description_window.erase()
                    item_description_window.refresh()
                    selected_item = None
                    continue
                elif key == ord("r"):
                    player.weapon = None
                    item_description_window.erase()
                    item_description_window.refresh()
                    selected_item = None
                    continue

                item_description_window.refresh()

        inventory_window.refresh()
        key = stdscr.getch()

        if key in (ord("i"), ord("I"), 27):
            if item_description_window:
                item_description_window.erase()
                item_description_window.refresh()
            inventory_window.clear()
            inventory_window.refresh()
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

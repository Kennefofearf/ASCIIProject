import curses
from player_module import Player
from data.affix_data import UNCOMMON_AFFIXES
from UI.colors import get_rarity_color
from UI.skill_tree_screen import open_skill_tree

def get_item_stat_bonus(item, stat):
    if not item:
        return 0

    total = item.get("base_stats", {}).get(stat, 0)

    for affix_id in item.get("affixes", []):
        affix_data = UNCOMMON_AFFIXES[affix_id]
        total += affix_data.get("affix_stats", {}).get(stat, 0)

    return total

def open_inventory_window(stdscr, player):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_item = None
    drop_item = False
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

            # if drop_item:
            #     inventory.remove(item)

        if selected_item:

            lvl = selected_item["lvl"]
            max_lvl = selected_item["max_lvl"]
            xp = selected_item["xp"]
            max_xp = selected_item["max_xp"]
            skill_points = selected_item["skill_points"]

            progress = xp / max_xp if max_xp > 0 else 0
            filled = int(progress * 10)
            # xp_bar = "=" * filled + "-" * (10 - filled)

            old_weapon = player.weapon
            new_weapon = selected_item

            stat_forecast_hp = (
                    player.max_hp - get_item_stat_bonus(old_weapon, "max_hp")
                    + get_item_stat_bonus(new_weapon, "max_hp")
            )
            stat_forecast_st = (
                    player.st - get_item_stat_bonus(old_weapon, "st")
                    + get_item_stat_bonus(new_weapon, "st")
            )
            stat_forecast_df = (
                    player.df - get_item_stat_bonus(old_weapon, "df")
                    + get_item_stat_bonus(new_weapon, "df")
            )

            item_color = get_rarity_color(selected_item)
            item_description_window = curses.newwin(height, description_width, start_y, description_x)
            item_description_window.box()

            detail_x = description_width // 9
            row = 5

            item_description_window.addstr(row, detail_x, selected_item["name"], curses.color_pair(item_color))
            row += 2

            item_description_window.addstr(row, detail_x, f"Lvl: {lvl} / {max_lvl}")
            row += 1

            item_description_window.addstr(row, detail_x, f"XP: {xp} / {max_xp}")
            row += 1

            # item_description_window.addstr(row, detail_x, f"[{xp_bar}]")
            # row += 1

            item_description_window.addstr(row, detail_x, f"Skill Points: {skill_points}")
            row += 2

            min_dmg = selected_item["min_dmg"]
            max_dmg = selected_item["max_dmg"]

            for affix_id in selected_item.get("affixes", []):
                affix_data = UNCOMMON_AFFIXES[affix_id]
                min_dmg += affix_data.get("min_dmg", 0)
                max_dmg += affix_data.get("max_dmg", 0)

            item_description_window.addstr(row, detail_x, f"DMG: {min_dmg} - {max_dmg}")
            row += 1

            for affix_id in selected_item.get("affixes", []):
                affix_data = UNCOMMON_AFFIXES[affix_id]

                for stat, value in affix_data.get("affix_stats", {}).items():
                    item_description_window.addstr(row, detail_x, f"{stat.upper()}: {value}")
                    row += 1

            row += 1

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
            row += 1
            item_description_window.addstr(row, detail_x, f"S(k)ill Tree")

            if key == ord("e"):
                player.weapon = selected_item
                item_description_window.erase()
                item_description_window.refresh()
                selected_item = None
                continue
            elif key == ord("r"):
                item_description_window.erase()
                item_description_window.refresh()
                player.weapon = None
                selected_item = None
                continue
            elif key == ord("k"):
                item_description_window.erase()
                item_description_window.refresh()
                open_skill_tree(stdscr, selected_item)

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

            if button_state & curses.BUTTON1_CLICKED:
                if mouse_y in item_rows:
                    selected_item = item_rows[mouse_y]

            if button_state & curses.BUTTON3_CLICKED:
                if mouse_y in item_rows:
                    drop_item = item_rows[mouse_y]
                    if player.weapon == drop_item:
                        player.weapon = None
                    inventory.remove(drop_item)

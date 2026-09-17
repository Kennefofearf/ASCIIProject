import curses
import time
from data.weapons_abilities_data import COMMON_WEAPON_ABILITIES
from UI.colors import UNAVAILABLE


def create_action_bar(stdscr):
    screen_h, screen_w = stdscr.getmaxyx()

    bar_y = 3
    bar_x = 60

    start_y = screen_h - 14
    start_x = (screen_w - bar_x) // 2

    action_bar = curses.newwin(bar_y, bar_x, start_y, start_x)

    return action_bar


def draw_action_bar(action_bar, player):
    action_bar.erase()
    action_bar.box()

    h, w = action_bar.getmaxyx()
    col = 2

    for slot, ability_id in player.ability_slots.items():
        if ability_id is not None:
            ability = COMMON_WEAPON_ABILITIES[ability_id]

            if not player.weapon or ability_id not in player.weapon.unlocked_abilities:
                action_bar.addstr(1, col, f"{slot}: {ability.name}", curses.color_pair(UNAVAILABLE))
            else:
                cooldown_end = player.cooldowns.get(ability_id, 0)
                remaining = cooldown_end - time.time()

                if remaining > 0:
                    action_bar.addstr(1, col, f"{slot}: {remaining:.1f}")

                else:
                    action_bar.addstr(1, col, f"{slot}: {ability.name}")
        else:
            action_bar.addstr(1, col, f"{slot}: None")

        col += 15

    action_bar.refresh()

import curses
from systems.weapon_skill_tree import generate_rarity_layout
from data.skill_node_data import COMMON_NODES
from UI.colors import get_rarity_color
import json


def dbg(data):
    with open("debug.txt", "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")


def draw_node(window, x, y, label, node, is_selected=False):
    height, width = window.getmaxyx()

    node_height = 5
    node_width = 7

    if y < 1 or y + node_height >= height:
        return

    if x < 1 or x + node_width >= width:
        return

    color = curses.A_REVERSE if is_selected else curses.A_NORMAL

    window.addstr(y, x, "_____", color)
    window.addstr(y + 1, x, "|     |", color)
    window.addstr(y + 2, x, f"|{label:^5}|", color)
    window.addstr(y + 3, x, "|_____|", color)

    rank = f"{node['points']}/{node['max_points']}"
    window.addstr(y + 4, x + 1, rank)


def draw_item_name(window, item, width):
    name = item["name"]
    item_color = get_rarity_color(item)
    xp = item["xp"]
    max_xp = item["max_xp"]

    title = f"{name}    {xp}/{max_xp}"
    window.addstr(1, max(1, (width - len(title)) / 2), title, item_color)

def draw_skill_tree_nodes(window, item, selected_slot, scroll):
    layout = item["skill_tree"]["layout"]

    for slot_index, position in enumerate(layout["slots"]):
        if position is None:
            continue

        y, x = position
        x -= scroll

        node = item["skill_tree"]["nodes"].get(slot_index)

        # if y == 6 | y == 7 | y == 8:
        #     node_data = TIER_CAPSTONE_NODES[node["node_id"]]
        #     label = node_data["name"][:5]
        #     is_selected = slot_index == selected_slot

        if node:
            node_data = COMMON_NODES[node["node_id"]]
            label = node_data["name"][:5]
            is_selected = slot_index == selected_slot

            draw_node(window, y, x, label, node, is_selected)


def open_skill_tree(stdscr, selected_item):
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    selected_slot = 0
    scroll_y = 0

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        skill_tree_window = curses.newwin(height, tree_width, start_y, tree_x)
        skill_tree_window.box()

        # draw_item_name(skill_tree_window, selected_item, width)
        draw_skill_tree_nodes(skill_tree_window, selected_item, selected_slot, scroll_y)
        skill_tree_window.refresh()

        key = stdscr.getch()

        if key == ord("k"):
            skill_tree_window.erase()
            skill_tree_window.refresh()
            break
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()

            if bstate & curses.BUTTON4_PRESSED:
                scroll_y = max(0, scroll_y - 2)

            elif bstate & curses.BUTTON5_PRESSED:
                scroll_y += 2


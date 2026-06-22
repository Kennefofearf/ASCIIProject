import curses
import random
from systems.loot_generator import get_rarity_color
from data.skill_tree_layout_data import LAYOUTS, RARITY_ORDER
from data.skill_node_data import COMMON_NODES

def draw_node(window, y, x, label, node, is_selected=False):
    color = curses.A_REVERSE if is_selected else curses.A_NORMAL

    window.addstr(y, x, "_____")
    window.addstr(y + 1, x, "|     |")
    window.addstr(y+ 2, x, f"|{label:^5}|")
    window.addstr(y + 3, x, "|_____|")

    rank = f"{node['points']}/{node['max_points']}"
    window.addstr(y + 4, x + 1, rank)

def draw_item_name(window, item, width):
    name = item["name"]
    item_color = get_rarity_color(item)
    xp = item["xp"]
    max_xp = item["max_xp"]

    title = f"{name}    {xp}/{max_xp}"
    window.addstr(1, max(1, (width - len(title)) / 2), title, curses.color_pair(item_color))

def generate_rarity_layout(rarity):
    slots = []
    connections = []
    previous_exits = []

    rarity_index = RARITY_ORDER.index(rarity)

    for rarity_name in RARITY_ORDER[:rarity_index + 1]:
        piece = random.choice(LAYOUTS[rarity_name])

        offset = len(slots)

        slots.extend(piece["slots"])

        for start, end in piece["connections"]:
            connections.append((start + offset, end + offset))

        current_entries = [slot + offset for slot in piece["entry_slots"]]
        current_exits = [slot + offset for slot in piece["exit_slots"]]

        for previous_slots in previous_exits:
            for current_slot in current_entries:
                connections.append((previous_slots, current_slot))

        previous_exits = current_exits

    return {
        "slots": slots,
        "connections": connections
    }

def draw_skill_tree_nodes(window, item, selected_slot):

    # if item["rarity"] == "white":
    #     white_id = random.choice(list(WHITE_LAYOUTS.keys()))
    layout = item["skill_tree"]["layout"]


    for slot_index, (y, x) in enumerate(layout["slots"]):
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
    selected_slot = 0

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        skill_tree_window = curses.newwin(height, tree_width, start_y, tree_x)
        skill_tree_window.box()

        draw_skill_tree_nodes(skill_tree_window, selected_item, selected_slot)

        skill_tree_window.refresh()

        key = stdscr.getch()

        if key == ord("k"):
            skill_tree_window.erase()
            skill_tree_window.refresh()
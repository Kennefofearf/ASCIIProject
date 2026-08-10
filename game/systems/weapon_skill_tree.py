import random
from data.skill_node_data import COMMON_NODES
from data.skill_tree_layout_data import RARITY_ORDER, LAYOUTS
# from game.systems.ability_logic import rebuild_abilities


def can_activate(player, skill_id):
    skill = COMMON_NODES["skill_id"]

    for req in skill.get("requires", []):
        if player.skill_tree[req]["points"] <= 0:
            return False

    return True


def assign_points(player, skill_id):
    skill_data = COMMON_NODES["skill_id"]
    skill_state = player.skill_tree["skill_id"]

    if skill_state["points"] >= skill_data["max_points"]:
        return False, "Maxed"

    if not can_activate(player, skill_id):
        return False, "Prerequisites not met."

    skill_state["points"] += 1

    for ability in skill_data.get("unlocks", []):
        player.abilities.add(ability)

    return True


def connect_tiers(connections, slots, previous_exits, current_entries):

    for previous_slot in previous_exits:
        previous_position = slots[previous_slot]

        if previous_position is None:
            continue

        _, previous_x = previous_position

        closest_entry = min(current_entries, key=lambda entry_slot: abs(slots[entry_slot][1] - previous_x))

        connections.append((previous_slot, closest_entry))


def generate_rarity_layout(rarity):
    slots = []
    connections = []
    previous_exits = []
    initial_entries = []
    capstones = {}

    rarity_index = RARITY_ORDER.index(rarity)

    for tier_index, rarity_name in enumerate(RARITY_ORDER[:rarity_index + 1]):
        piece = random.choice(LAYOUTS[rarity_name])

        offset = len(slots)

        global_capstone = piece["capstone_slot"] + offset

        slots.extend(piece["slots"])

        if piece["slots"][piece["capstone_slot"]] is not None:
            capstones[global_capstone] = rarity_name

        for start, end in piece["connections"]:
            connections.append((start + offset, end + offset))

        current_entries = [slot + offset for slot in piece["entry_slots"]]
        current_exits = [slot + offset for slot in piece["exit_slots"]]

        # Only the first tier starts available
        if tier_index == 0:
            initial_entries = current_entries

        # for previous_slots, current_slot in zip(previous_exits, current_entries):
        #     connections.append((previous_slots, current_slot))

        if previous_exits:
            connect_tiers(connections, slots, previous_exits, current_entries)

        previous_exits = current_exits

    return {
        "slots": slots,
        "connections": connections,
        "entry_slots": initial_entries,
        "exit_slots": previous_exits,
        "capstones": capstones
    }

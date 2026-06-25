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

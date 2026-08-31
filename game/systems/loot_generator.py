import random
import json

from item_module import Item
from data.weapon import Weapon
from armor_module import Armor
from data.equipment_data import EQUIPMENT
from data.affix_data import GREEN_AFFIXES, BLUE_AFFIXES, YELLOW_AFFIXES, PURPLE_AFFIXES
from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES
from systems.weapon_skill_tree import generate_rarity_layout


def dbg(data):
    with open("debug.txt", "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")


def create_affix_pool(item_level):
    pools = []

    if item_level >= 1:
        pools.append(GREEN_AFFIXES)

    if item_level >= 21:
        pools.append(BLUE_AFFIXES)

    if item_level >= 41:
        pools.append(YELLOW_AFFIXES)

    if item_level >= 51:
        pools.append(PURPLE_AFFIXES)

    return pools


def merge_affix_pools(pools):
    merged = {}

    for pool in pools:
        merged.update(pool)

    return merged


def filter_affixes_by_item_type(affixes, item_type):
    filtered = {}

    for affix_id, affix_data in affixes.items():
        allowed = affix_data.get("item_type", [])

        if item_type in allowed:
            filtered[affix_id] = affix_data

    return filtered


def choose_affixes(item_level, item_type):
    pools = create_affix_pool(item_level)
    available_affixes = merge_affix_pools(pools)

    prefixes = {"green": [], "blue": [], "yellow": [], "purple": []}
    suffixes = {"green": [], "blue": [], "yellow": [], "purple": []}

    for affix_id, affix_data in available_affixes.items():

        if item_type not in affix_data.item_type:
            continue

        if affix_data.affix_type == "prefix":
            prefixes[affix_data.rarity].append(affix_id)

        elif affix_data.affix_type == "suffix":
            suffixes[affix_data.rarity].append(affix_id)

    rolled_affixes = []

    # has_suffix = random.random() <= 0.2
    # has_prefix = random.random() <= 0.2

    roll = random.random()

    if roll <= 0.01:
        rarity = "purple"
    elif roll <= 0.06:
        rarity = "yellow"
    elif roll <= 0.21:
        rarity = "blue"
    else:
        rarity = None

    green_roll_1 = random.random()
    green_roll_2 = random.random()

    if green_roll_1 <= 0.25:
        choices = []

        if prefixes["green"]:
            choices.append(prefixes["green"])
        if suffixes["green"]:
            choices.append(suffixes["green"])

        if choices:
            chosen_pool = random.choice(choices)
            chosen_affix = random.choice(chosen_pool)
            rolled_affixes.append(chosen_affix)

    if green_roll_2 <= 0.25:
        choices = []

        if prefixes["green"]:
            choices.append(prefixes["green"])
        if suffixes["green"]:
            choices.append(suffixes["green"])

        if choices:
            chosen_pool = random.choice(choices)
            chosen_affix = random.choice(chosen_pool)
            if chosen_affix not in rolled_affixes:
                rolled_affixes.append(chosen_affix)

    choices = []

    if rarity and prefixes[rarity]:
        choices.append(prefixes[rarity])
    if rarity and suffixes[rarity]:
        choices.append(suffixes[rarity])

    if choices:
        chosen_pool = random.choice(choices)
        chosen_affix = random.choice(chosen_pool)
        rolled_affixes.append(chosen_affix)

    return rolled_affixes, available_affixes


RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]


def calculate_rarity(item, available_affixes):
    highest_rarity = "white"

    for affix_id in item.affixes:
        affix = available_affixes[affix_id]

        if RARITY_ORDER.index(affix.rarity) > RARITY_ORDER.index(highest_rarity):
            highest_rarity = affix.rarity

    return highest_rarity


def apply_affix_stats(item, affix_stats):
    for stat_name, value in affix_stats.get("affix_stats", {}).items():
        item["base_stats"][stat_name] = item["base_stats"].get(stat_name, 0) + value

def build_item_name(base_name, affix_ids, affix_pool):
    prefixes = []
    suffixes = []

    for affix_id in affix_ids:
        affix = affix_pool[affix_id]

        if affix.affix_type == "prefix":
            prefixes.append(affix.name)

        elif affix.affix_type == "suffix":
            suffixes.append(affix.name)

    name_parts = []

    if prefixes:
        name_parts.extend(prefixes)

    name_parts.append(base_name)

    if suffixes:
        name_parts.extend(suffixes)

    return " ".join(name_parts)

def get_skill_node_count(item):
    rarity = item.get("rarity", "white")

    rarity_tiers = {
        "white": 7,
        "green": 14,
        "blue": 21,
        "yellow": 28,
        "purple": 35
    }

    tier_bonus = rarity_tiers.get(rarity, 0)

    return 7 + (tier_bonus * 7)


def generate_item_skill_tree(base, layout):
    valid_slot_indexes = []

    for index, position in enumerate(layout["slots"]):
        if position is not None:
            valid_slot_indexes.append(index)

    node_count = len(valid_slot_indexes)

    possible_nodes = {}

    item_tags = base.get("skill_tags", [])

    for node_id, node_data in COMMON_NODES.items():
        node_tags = node_data.skill_tags

        if any(tag in item_tags for tag in node_tags):
            possible_nodes[node_id] = node_data

    # chosen_node_ids = random.sample(
    #     list(possible_nodes.keys()),
    #     min(node_count, len(possible_nodes))
    # )

    nodes = {}

    for slot_index in valid_slot_indexes:
        capstone_rarity = layout["capstones"].get(slot_index)

        if capstone_rarity:
            node_pool = CAPSTONE_NODES[capstone_rarity]
            node_type = "capstone"
        else:
            node_pool = possible_nodes
            node_type = "common"

        node_id = random.choice(list(node_pool.keys()))

        entry_slots = layout.get("entry_slots", [])

        nodes[slot_index] = {
            "node_id": node_id,
            "node_type": node_type,
            "capstone_rarity": capstone_rarity,
            "points": 0,
            "max_points": node_pool[node_id].max_points,
            "available": slot_index in entry_slots

        }

    return nodes


def create_item_instance(base):
    if base["type"] == "weapon":
        return Weapon()

    if base["type"] == "armor":
        return Armor()

    return Item()


def generate_item(base_id, item_level):
    base = EQUIPMENT[base_id]

    item = create_item_instance(base)

    # from weapons_data, EQUIPMENT definition

    item.id = f"{base_id}_{random.randint(1000, 9999)}"
    item.name = base["name"]
    item.type = base["type"]

    if item.type == "weapon":

        item.min_dmg = base["min_dmg"]
        item.max_dmg = base["max_dmg"]
        item.attack_cooldown = base["attack_cooldown"]

    if item.type == "armor":
        item.base_ac = base["ac"]
        item.slot = base["slot"]

    item.base_stats = base.get("base_stats", {})
    item.item_lvl = item_level
    item.xp = base.get("xp", 0)
    item.max_xp = base.get("max_xp", 100)
    item.lvl = base.get("lvl", 1)
    item.max_lvl = base.get("max_lvl", 10)
    item.skill_tags = base.get("skill_tags", [])
    item.abilities = base.get("abilities", [])

    item.affixes, available_affixes = choose_affixes(item_level=item_level, item_type=item.type)

    if item.type == "weapon" and item.affixes:
        dmg_bonus = random.choice([0, 1, 2])
        item.min_dmg += dmg_bonus
        item.max_dmg += dmg_bonus

    item.rarity = calculate_rarity(item.affixes)

    layout = generate_rarity_layout(item.rarity)

    item.skill_tree = {
        "layout": layout,
        "nodes": generate_item_skill_tree(base, layout)
    }

    for affix_id in item.affixes:
        affix = available_affixes[affix_id]
        apply_affix_stats(item, affix.affix_stats)

    item.name = build_item_name(base["name"], item.affixes, available_affixes)

    return item

def roll_item_drop(enemy):
    drop_chance = getattr(enemy, "drop_chance", 0.25)

    if random.random() > drop_chance:
        return None

    item_level = getattr(enemy, "level", 1)

    base_id = random.choice(list(EQUIPMENT.keys()))

    return generate_item(base_id, item_level)



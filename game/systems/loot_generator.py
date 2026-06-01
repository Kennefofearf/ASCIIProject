import curses
import random
from data.weapons_data import EQUIPMENT
from data.item_base import create_item_base
from data.affix_data import UNCOMMON_AFFIXES
from data.rarities_data import RARITIES
from data.skill_node_data import COMMON_NODES

# def roll_value(value):
#     if isinstance(value, list):
#         return random.randint(value[0], value[1])
#
#     return value
#
# def roll_stats(stat_block, stat_multi):
#     rolled = {}
#
#     for stat_name, value in stat_block.items():
#         rolled_value = roll_value(value)
#         rolled[stat_name] = max(0, int(rolled_value * stat_multi))
#
#     return rolled
import json


def dbg(data):
    with open("debug.txt", "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")

def create_affix_pool(item_level):
    pools = []

    if item_level >= 5:
        pools.append(UNCOMMON_AFFIXES)

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

    prefixes = []
    suffixes = []

    for affix_id, affix_data in available_affixes.items():

        allowed = affix_data.get("item_type", [])

        if item_type not in allowed:
            continue

        if affix_data.get("type") == "prefix":
            prefixes.append(affix_id)

        elif affix_data.get("type") == "suffix":
            suffixes.append(affix_id)

    rolled_affixes = []

    has_suffix = random.random() <= 0.2
    has_prefix = random.random() <= 0.2

    if has_prefix and prefixes:
        rolled_affixes.append(random.choice(prefixes))

    if has_suffix and suffixes:
        rolled_affixes.append(random.choice(suffixes))

    return rolled_affixes, available_affixes

def calculate_rarity(possible_affixes):
    affix_count = len(possible_affixes)

    if affix_count <= 0:
        return "white"
    elif affix_count == 1:
        return "green"

    return "rare"

def apply_affix_stats(item, affix_stats):
    for stat_name, value in affix_stats.get("affix_stats", {}).items():
        item["base_stats"][stat_name] = item["base_stats"].get(stat_name, 0) + value

def build_item_name(base_name, affix_ids, affix_pool):
    prefixes = []
    suffixes = []

    for affix_id in affix_ids:
        affix = affix_pool[affix_id]

        if affix.get("type") == "prefix":
            prefixes.append(affix["name"])

        elif affix.get("type") == "suffix":
            suffixes.append(affix["name"])

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

def generate_item_skill_tree(item, base):
    node_count = get_skill_node_count(item)
    item_tags = base.get("skill_tags", [])

    possible_nodes = {}

    for node_id, node_data in COMMON_NODES.items():
        node_tags = node_data.get("skill_tags", [])

        if any(tag in item_tags for tag in node_tags):
            possible_nodes[node_id] = node_data

    chosen_node_ids = random.sample(
        list(possible_nodes.keys()),
        min(node_count, len(possible_nodes))
    )

    skill_tree = {}

    for node_id in chosen_node_ids:

        node_data = possible_nodes[node_id]

        skill_tree[node_id] = {
            "name": node_data.get("name", ""),
            "tooltip": node_data.get("tooltip", ""),
            "points": 0,
            "max_points": node_data.get("max_points", 1),
            "active": False,
            "stats": dict(node_data.get("stats", {})),
            "requires": list(node_data.get("requires", [])),
            "unlocks": list(node_data.get("unlocks", [])),
            "skill_tags": list(node_data.get("skill_tags", []))
        }

    return skill_tree

def generate_item(base_id, item_level):
    base = EQUIPMENT[base_id]

    item = create_item_base()

    # from weapons_data, EQUIPMENT definition

    item["id"] = f"{base_id}_{random.randint(1000, 9999)}"
    item["name"] = base["name"]
    item["type"] = base["type"]
    item["min_dmg"] = base["min_dmg"]
    item["max_dmg"] = base["max_dmg"]
    item["base_stats"] = base.get("base_stats", {})
    item["item_level"] = item_level
    item["xp"] = base.get("xp", 0)
    item["max_xp"] = base.get("max_xp", 100)
    item["lvl"] = base.get("lvl", 1)
    item["max_lvl"] = base.get("max_lvl", 7)
    item["skill_tags"] = base.get("skill_tags", [])
    item["skill_nodes"] = generate_item_skill_tree(item, base)

    item["affixes"], available_affixes = choose_affixes(item_level=item_level, item_type=item["type"])

    item["rarity"] = calculate_rarity(item["affixes"])

    item["abilities"] = base.get("abilities", [])

    for affix_id in item["affixes"]:
        affix = available_affixes[affix_id]
        apply_affix_stats(item, affix.get("affix_stats", {}))

    item["name"] = build_item_name(base["name"], item["affixes"], available_affixes)

    return item

def get_rarity_color(item):
    rarity = item.get("rarity")
    item_level = item.get("item_level")

    # item level determines possible rarity

    if rarity == "white":
        return 0
    elif rarity == "green" and item_level >= 5:
        return 3

    return 0

def roll_item_drop(enemy):
    drop_chance = getattr(enemy, "drop_chance", 0.25)

    if random.random() > drop_chance:
        return None

    item_level = getattr(enemy, "level", 1)

    base_id = random.choice(list(EQUIPMENT.keys()))

    return generate_item(base_id, item_level)



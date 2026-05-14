import random

from game.data.weapons_data import EQUIPMENT
from game.data.item_base import create_item_base
from game.data.affix_data import UNCOMMON_AFFIXES
from game.data.rarities_data import RARITIES

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

def choose_affixes(count, item_level):
    affix_pools = create_affix_pool(item_level)
    available_affixes = merge_affix_pools(affix_pools)

    possible_affixes = list(available_affixes.keys())

    if count <= 0:
        return []

    count = min(count, len(possible_affixes))

    return random.sample(possible_affixes, count)

def apply_affix_stats(item, affix_id):
    affix = UNCOMMON_AFFIXES[affix_id]

    for stat_name, value in affix.get("stats", {}).items():
        item["stats"][stat_name] = item["stats"].get(stat_name, 0)

def build_item_name(base_name, affix_ids):
    prefixes = []
    suffixes = []

    for affix_id in affix_ids:
        affix = UNCOMMON_AFFIXES[affix_id]

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

def generate_item(base_id, rarity_id="common", item_lvl=1):
    base = EQUIPMENT[base_id]
    rarity = RARITIES[rarity_id]

    item = create_item_base()

    item["id"] = f"{rarity_id}_{base_id}_{random.randint(1000, 9999)}"
    item["name"] = base["name"]
    item["type"] = base["type"]
    item["slot"] = base["slot"]
    item["base"] = base["base"]
    item["rarity"] = rarity_id
    item["item_level"] = item_lvl

    item["base_stats"] = base.get("base_stats", {})
    item["abilities"] = base.get("abilities", [])

    affix_count = rarity.get("affix_count", 0)
    item["affixes"] = choose_affixes(affix_count)

    for affix_id in item["affixes"]:
        apply_affix_stats(item, affix_id)

    item["tags"] = list(base.get("tags", []))

    item["name"] = build_item_name(base["name"], item["affixes"])

    return item

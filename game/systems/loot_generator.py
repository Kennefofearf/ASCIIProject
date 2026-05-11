import random

from game.data.weapons_data import WEAPONS
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
def choose_affixes(count):
    if count <= 0:
        return []

    possible_affixes = list(UNCOMMON_AFFIXES.keys())
    count = min(count, len(possible_affixes))

    return random.sample(possible_affixes, count)

def generate_item(base_id):
    base = WEAPONS[base_id]
    item = create_item_base()

    item["id"] = base_id
    item["name"] = base["name"]
    item["type"] = base["type"]
    item["slot"] = base["slot"]
    item["base"] = base["base"]
    item["rarity"] = base["rarity"]
    item["item_level"] = base["item_level"]
    item["rolled_stats"] = base["rolled_stats"]
    item["abilities"] = base["abilities"]
    item["affixes"] = base["affixes"]
    item["tags"] = base["tags"]

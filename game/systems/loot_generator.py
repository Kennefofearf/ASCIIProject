from game.data.weapons_data import WEAPONS
from game.data.item_base import create_item_base

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
    item["base_stats"] = base["base_stats"]
    item["abilities"] = base["abilities"]
    item["affixes"] = base["affixes"]
    item["tags"] = base["tags"]

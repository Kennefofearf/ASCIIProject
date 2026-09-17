from data.weapon import Weapon
from modules.armor_module import Armor
from systems.item_persistence.skill_tree_from_dict import skill_tree_from_dict


def item_dict_to_item(data):
    if data["type"] == "weapon":
        item = Weapon()
        item.base_min_dmg = data["base_min_dmg"]
        item.base_max_dmg = data["base_max_dmg"]
        item.attack_cooldown = data["attack_cooldown"]

    elif data["type"] == "armor":
        item = Armor()
        item.base_ac = data["base_ac"]
        item.slot = data["slot"]

    item.id = data["id"]
    item.name = data["name"]
    item.type = data["type"]
    item.rarity = data["rarity"]
    item.base_stats = data["base_stats"]
    item.item_lvl = data["item_lvl"]
    item.xp = data["xp"]
    item.max_xp = data["max_xp"]
    item.lvl = data["lvl"]
    item.max_lvl = data["max_lvl"]
    item.skill_points = data["skill_points"]
    item.skill_tags = data["skill_tags"]
    item.affixes = data["affixes"]
    item.skill_tree = skill_tree_from_dict(data["skill_tree"])

    return item

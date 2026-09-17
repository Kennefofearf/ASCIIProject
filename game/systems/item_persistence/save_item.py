def item_to_dict(item):
    data = {
        "id": item.id,
        "name": item.name,
        "type": item.type,
        "rarity": item.rarity,
        "base_stats": item.base_stats,
        "item_lvl": item.item_lvl,
        "xp": item.xp,
        "max_xp": item.max_xp,
        "lvl": item.lvl,
        "max_lvl": item.max_lvl,
        "skill_points": item.skill_points,
        "skill_tags": item.skill_tags,
        "affixes": item.affixes,
        "skill_tree": item.skill_tree
    }

    if item.type == "weapon":
        data["base_min_dmg"] = item.base_min_dmg
        data["base_max_dmg"] = item.base_max_dmg
        data["attack_cooldown"] = item.attack_cooldown

    if item.type == "armor":
        data["base_ac"] = item.base_ac
        data["slot"] = item.slot

    return data

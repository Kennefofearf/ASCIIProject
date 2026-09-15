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
        "affixes": []
    }

    if item.type == "weapon":
        data["min_dmg"] = item.min_dmg
        data["max_dmg"] = item.max_dmg
        data["attack_cooldown"] = item.attack_cooldown

    return data

def get_item_level_multiplier(item_lvl, rarity):
    if rarity == "green":
        if item_lvl <= 20:
            return 1.0
        elif item_lvl <= 30:
            return 1.5
        elif item_lvl <= 40:
            return 2.0
        elif item_lvl <= 50:
            return 2.5
        else:
            return 3.0
    elif rarity == "blue":
        if item_lvl <= 40:
            return 1.0
        elif item_lvl <= 50:
            return 1.5
        else:
            return 2.0
    else:
        return 1.0


def get_base_ac_multiplier(item_lvl):
    if item_lvl <= 20:
        return 1.0
    elif item_lvl <= 30:
        return 1.5
    elif item_lvl <= 40:
        return 2.0
    elif item_lvl <= 50:
        return 2.5
    else:
        return 3.0


def get_base_dmg_multiplier(item_lvl):
    if item_lvl <= 20:
        return 1.0
    elif item_lvl <= 30:
        return 1.5
    elif item_lvl <= 40:
        return 2.0
    elif item_lvl <= 50:
        return 2.5
    else:
        return 3.0


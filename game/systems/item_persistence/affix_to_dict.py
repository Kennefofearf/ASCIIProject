def affix_to_dict(affix):
    data = {
        "name": affix.name,
        "affix_type": affix.affix_type,
        "affix_stats": affix.affix_stats,
        "ac": affix.ac,
        "min_dmg": affix.min_dmg,
        "max_dmg": affix.max_dmg,
        "item_type": affix.item_type,
        "rarity": affix.rarity
    }

    return data
import random

UNCOMMON_AFFIXES = {
        "of Balance": {
            "name": "of Balance",
            "affix_stats": {"max_hp": 5, "st": 5, "df": 5},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2]),
            "slots": 7
        }
    }
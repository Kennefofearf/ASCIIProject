import random

UNCOMMON_AFFIXES = {
        "of Balance": {
            "name": "of Balance",
            "type": "suffix",
            "affix_stats": {"max_hp": 5, "st": 5, "df": 5},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2]),
            "slots": 7,
            "item_types": ["weapons", "armor"]
        },
        "of Minor Constitution": {
            "name": "of Minor Constitution",
            "type": "suffix",
            "affix_stats": {"max_hp": 15, "st": 0, "df": 0},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2]),
            "slots": 7,
            "item_types": ["weapons", "armor"]
        },
        "of Perseverance": {
            "name": "of Perseverance",
            "type": "suffix",
            "affix_stats": {"max_hp": 9, "st": 0, "df": 7},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2]),
            "slots": 7,
            "item_types": ["weapons", "armor"]
        },
        "of the Rotund Fool": {
            "name": "of the Rotund Fool",
            "type": "suffix",
            "affix_stats": {"max_hp": 20, "st": -10, "df": -7},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2]),
            "slots": 7,
            "item_types": ["weapons", "armor"]
        }
    }

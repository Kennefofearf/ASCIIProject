import random
from player_module import Player

class Affixes:

    def __init__(self, name, affix_stats, min_dmg, max_dmg, xp, common_skills, lvl):
        self.name = name
        self.stats = affix_stats
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    AFFIXES = {
        "of Balance": {
            "name": "of Balance",
            "affix_stats": {"max_hp": 5, "st": 5, "df": 5},
            "min_dmg": random.choice([0, 1, 2]),
            "max_dmg": random.choice([0, 1, 2])
        }
    }
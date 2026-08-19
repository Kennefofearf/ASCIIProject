import random
from affix_module import Affix

UNCOMMON_AFFIXES = {
        "of_balance": Affix(
            name="of Balance",
            affix_type="suffix",
            affix_stats={"max_hp": 5, "st": 5, "df": 5},
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([0, 1, 2]),
            item_type=["weapon", "armor"]
        ),
        "of_minor_constitution": Affix(
            name="of Minor Constitution",
            affix_type="suffix",
            affix_stats={"max_hp": 15, "st": 0, "df": 0},
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([0, 1, 2]),
            item_type=["weapon", "armor"]
        ),
        "of_perseverance": Affix(
            name="of Perseverance",
            affix_type="suffix",
            affix_stats={"max_hp": 9, "st": 0, "df": 7},
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([0, 1, 2]),
            item_type=["weapon", "armor"]
        ),
        "of_the_rotund_fool": Affix(
            name="of the Rotund Fool",
            affix_type="suffix",
            affix_stats={"max_hp": 20, "st": -10, "df": -7},
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([0, 1, 2]),
            item_type=["weapon", "armor"]
        )
    }

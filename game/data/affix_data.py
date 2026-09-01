import random
from affix_module import Affix

# "max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0

GREEN_AFFIXES = {
        "of_balance": Affix(
            name="of Balance",
            affix_type="suffix",
            affix_stats={"max_hp": 5, "st": 5, "df": 5},
            ac=random.choice([0, 1]),
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        ),
        "of_minor_constitution": Affix(
            name="of Minor Constitution",
            affix_type="suffix",
            affix_stats={"max_hp": 15},
            ac=random.choice([0, 1]),
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        ),
        "of_perseverance": Affix(
            name="of Perseverance",
            affix_type="suffix",
            affix_stats={"max_hp": 9, "df": 7},
            ac=random.choice([0, 1]),
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        ),
        "of_the_rotund_fool": Affix(
            name="of the Rotund Fool",
            affix_type="suffix",
            affix_stats={"max_hp": 20, "st": -10},
            ac=1,
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        ),
        "sharp": Affix(
            name="Sharp",
            affix_type="prefix",
            affix_stats={"st": 1},
            ac=0,
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon"],
            rarity="green"
        ),
        "agile": Affix(
            name="Agile",
            affix_type="prefix",
            affix_stats={"ev": 2},
            ac=random.choice([0, 1]),
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        ),
        "genius's": Affix(
            name="Genius's",
            affix_type="prefix",
            affix_stats={"mp": 5},
            ac=0,
            min_dmg=random.choice([0, 1, 2]),
            max_dmg=random.choice([1, 2, 3]),
            item_type=["weapon", "armor"],
            rarity="green"
        )
    }

BLUE_AFFIXES = {
    "sir_lloyd's": Affix(
            name="Sir Lloyd's",
            affix_type="prefix",
            affix_stats={"st": 15},
            ac=0,
            min_dmg=random.choice([3, 4, 5]),
            max_dmg=random.choice([4, 5, 6]),
            item_type=["weapon", "armor"],
            rarity="blue"
        )}

YELLOW_AFFIXES = {
    "of_the_burning_moonlight": Affix(
            name="of the Burning Moonlight",
            affix_type="suffix",
            affix_stats={"max_hp": 200, "st": 26, "df": 15},
            ac=8,
            min_dmg=random.choice([8, 9, 10]),
            max_dmg=random.choice([9, 10, 11]),
            item_type=["weapon", "armor"],
            rarity="yellow"
        )}

PURPLE_AFFIXES = {
    "ancient_being's": Affix(
            name="Ancient Being's",
            affix_type="prefix",
            affix_stats={"max_hp": 350, "mp": 55, "ev": 5, "hp_rr": 2.0, "hp_ra": 15},
            ac=3,
            min_dmg=random.choice([23, 24, 25]),
            max_dmg=random.choice([24, 25, 26]),
            item_type=["weapon", "head"],
            rarity="purple"
        )}

ALL_AFFIXES = {
    **GREEN_AFFIXES,
    **BLUE_AFFIXES,
    **YELLOW_AFFIXES,
    **PURPLE_AFFIXES
}

import curses
import random
from player_module import Player

class Weapons:

    def __init__(self, name, min_dmg, max_dmg, xp, skill_slots, lvl, max_lvl, base_stats, affix):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.base_stats = base_stats
        self.affix = affix
        self.xp = xp
        self.skill_slots = skill_slots
        self.lvl = lvl
        self.max_lvl = max_lvl

        WEAPONS = {
            "Dagger": {
                "name": "Dagger" + f"{affix}",
                "affix": affix,
                "min_dmg": 2,
                "max_dmg": 6,
                "max_hp": 0,
                "base_stats": {"max_hp": 0, "st": 0, "df": 0},
                "skill_slots": 7,
                "lvl": 1,
                "max_lvl": 10
            }
        }


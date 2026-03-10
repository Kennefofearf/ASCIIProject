import curses
import random
from player_module import Player

class Weapons:

    def __init__(self, name, min_dmg, max_dmg, xp, skill_tree, lvl, max_lvl, base_stats, affix, affix_stats):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.base_stats = base_stats
        self.affix = affix
        self.affix_stats = affix_stats
        self.xp = xp
        self.skill_tree = skill_tree
        self.lvl = lvl
        self.max_lvl = max_lvl

    @property
    def name(self):
        if self.affix:
            return f"{self.name} {self.affix}"
        return self.name

    def min_dmg(self, affix_min_dmg):
        if self.affix:
            self.min_dmg += self.affix_min_dmg.get(affix_min_dmg, 0)
            return self.min_dmg
        return self.min_dmg

    def max_dmg(self, affix_max_dmg):
        if self.affix:
            self.max_dmg += self.affix_max_dmg.get(affix_max_dmg, 0)
            return self.max_dmg
        return self.max_dmg

    def affix_stats(self, affix_stats):
        self.base_stats.get(affix_stats, 0)

    def skill_tree_bonus(self, stats):
        total = 0
        for node in self.skill_tree:
            if node.stats == stats:
                total += node.bonus()
        return total

    def total_bonus(self, stat):
        return (
            self.base_stats(stat)
            + self.affix_stats(stat)
            + self.skill_tree_bonus(stat)
        )



        WEAPONS = {
            "Dagger": {
                "name": "Dagger" + f"{affix}",
                "affix": affix,
                "min_dmg": 2,
                "max_dmg": 6,
                "max_hp": 0,
                "base_stats": {"max_hp": 0, "st": 0, "df": 0},
                "skill_tree": 7,
                "lvl": 1,
                "max_lvl": 10
            }
        }


import curses
import random
from player_module import Player

class Weapons:

    def __init__(self, name, min_dmg, max_dmg, xp, skill_slots, lvl, base_stats, affix, affix_stats):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.base_stats = base_stats
        self.affix = affix
        self.affix_stats = affix_stats
        self.xp = xp
        self.skill_slots = skill_slots
        self.lvl = lvl


import curses
import random
from player_module import Player

class Weapons:

    def __init__(self, name, min_dmg, max_dmg, xp, skills, lvl, capstone_skill, skill_slots):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.xp = xp
        self.skills = skills
        self.capstone_skill = capstone_skill
        self.skill_slots = skill_slots
        self.lvl = lvl


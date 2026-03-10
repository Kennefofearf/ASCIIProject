import random
from player_module import Player

class Attributes:

    def __init__(self, name, st, df, max_hp, min_dmg, max_dmg, xp, common_skills, lvl):
        self.name = name
        self.st = st
        self.df = df
        self.max_hp = max_hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def of_balance(self):
        self.name = "of Balance"
        Player.max_hp += 5
        Player.st += 5
        Player.df += 5
        self.min_dmg += random.choice[0, 1, 2]
        self.max_dmg += random.choice[0, 1, 2]
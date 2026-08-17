import random


class Affix:

    def __init__(self, name, affix_type, affix_stats, min_dmg, max_dmg, item_type):
        self.name = name
        self.affix_type = affix_type
        self.affix_stats = affix_stats
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        # self.slots = slots
        self.item_type = item_type
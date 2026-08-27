from item_module import Item
from data.affix_data import UNCOMMON_AFFIXES


class Armor(Item):

    def __init__(self):
        super().__init__()

        self.base_ac = 0
        self.slot = ""

    @property
    def ac(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = UNCOMMON_AFFIXES[affix_id]
            bonus += affix.ac

        return self.base_ac + bonus
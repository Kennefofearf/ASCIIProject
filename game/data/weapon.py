from data.affix_data import GREEN_AFFIXES
from item_module import Item


class Weapon(Item):

    def __init__(self):
        super().__init__()

        self._min_dmg = 0
        self._max_dmg = 0
        self.attack_cooldown = 1

    @property
    def min_dmg(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = GREEN_AFFIXES.get(affix_id, {})
            bonus += affix.min_dmg

        return self._min_dmg + bonus

    @min_dmg.setter
    def min_dmg(self, value):
        self._min_dmg = value

    @property
    def max_dmg(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = GREEN_AFFIXES.get(affix_id, {})
            bonus += affix.max_dmg

        return self._max_dmg + bonus

    @max_dmg.setter
    def max_dmg(self, value):
        self._max_dmg = value

    def calculate_item_xp_requirement(self):
        average_attack_cooldown = 1.0

        weapon_speed = self.attack_cooldown

        xp_requirement = (average_attack_cooldown / weapon_speed) * 100

        return round(xp_requirement)







from data.affix_data import ALL_AFFIXES
from item_module import Item
from systems.item_scaling import get_item_level_multiplier, get_base_dmg_multiplier


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
            affix = ALL_AFFIXES.get(affix_id)
            multiplier = get_item_level_multiplier(self.item_lvl, affix.rarity)
            bonus += round(affix.min_dmg * multiplier)

        base_multiplier = get_base_dmg_multiplier(self.item_lvl)
        scaled_base = round(self._min_dmg * base_multiplier)

        return scaled_base + bonus

    @min_dmg.setter
    def min_dmg(self, value):
        self._min_dmg = value

    @property
    def max_dmg(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = ALL_AFFIXES.get(affix_id)
            multiplier = get_item_level_multiplier(self.item_lvl, affix.rarity)
            bonus += round(affix.max_dmg * multiplier)

        base_multiplier = get_base_dmg_multiplier(self.item_lvl)
        scaled_base = round(self._max_dmg * base_multiplier)

        return scaled_base + bonus

    @max_dmg.setter
    def max_dmg(self, value):
        self._max_dmg = value

    def calculate_item_xp_requirement(self):
        average_attack_cooldown = 1.0

        weapon_speed = self.attack_cooldown

        xp_requirement = (average_attack_cooldown / weapon_speed) * 100

        return round(xp_requirement)







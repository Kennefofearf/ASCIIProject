from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES
from data.affix_data import UNCOMMON_AFFIXES
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
            affix = UNCOMMON_AFFIXES.get(affix_id, {})
            bonus += affix.get("affix_stats", {}).get("min_dmg", 0)

        return self._min_dmg + bonus

    @min_dmg.setter
    def min_dmg(self, value):
        self._min_dmg = value

    @property
    def max_dmg(self):
        bonus = 0

        for affix_id in self.affixes:
            affix = UNCOMMON_AFFIXES.get(affix_id, {})
            bonus += affix.get("affix_stats", {}).get("max_dmg", 0)

        return self._max_dmg + bonus

    @max_dmg.setter
    def max_dmg(self, value):
        self._max_dmg = value

    # Using static methods until refactor

    @staticmethod
    def skill_tree_bonus(item, stat):
        nodes = item.skill_tree["nodes"].values()

        total = 0

        for node in nodes:

            if node.get("node_type") == "capstone":
                rarity = node["capstone_rarity"]
                node_data = CAPSTONE_NODES[rarity][node["node_id"]]
            else:
                node_data = COMMON_NODES[node["node_id"]]

            stat_value = node_data["stats"].get(stat, 0)
            total += stat_value * node["points"]

        return total

    @staticmethod
    def total_bonus(item, stat):
        if not item:
            return 0

        total = item.base_stats.get(stat, 0)

        for affix_id in item.affixes:
            affix_data = UNCOMMON_AFFIXES.get(affix_id, {})
            total += affix_data.get("affix_stats", {}).get(stat, 0)

        total += Weapon.skill_tree_bonus(item, stat)

        return total

    @staticmethod
    def calculate_item_xp_requirement(item):
        if item is None:
            return 0

        average_attack_cooldown = 1.0

        weapon_speed = item.attack_cooldown

        xp_requirement = (average_attack_cooldown / weapon_speed) * 100

        return round(xp_requirement)

    @staticmethod
    def level_up_item(item):
        item.xp -= item.max_xp
        item.lvl += 1
        item.skill_points += 1
        item.max_xp = Weapon.calculate_item_xp_requirement(item)

        if item.lvl >= item.max_lvl:
            item.xp = 0

    @staticmethod
    def gain_item_xp(item, amount):
        if item.lvl >= item.max_lvl:
            return

        item.xp += amount

        while item.xp >= item.max_xp:
            Weapon.level_up_item(item)






from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES, STAT_NAMES
from data.affix_data import UNCOMMON_AFFIXES

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

    @staticmethod
    def skill_tree_bonus(item, stat):
        nodes = item["skill_tree"]["nodes"].values()

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

        total = item.get("base_stats", {}).get(stat, 0)

        for affix_id in item.get("affixes", []):
            affix_data = UNCOMMON_AFFIXES.get(affix_id, {})
            total += affix_data.get("affix_stats", {}).get(stat, 0)

        total += Weapons.skill_tree_bonus(item, stat)

        return total

    @staticmethod
    def calculate_item_xp_requirement(item):
        if item is None:
            return 0

        average_attack_cooldown = 1.0

        weapon_speed = item["attack_cooldown"]

        xp_requirement = (average_attack_cooldown / weapon_speed) * 100

        return round(xp_requirement)

    @staticmethod
    def level_up_item(item):
        item["xp"] -= item["max_xp"]
        item["lvl"] += 1
        item["skill_points"] += 1
        item["max_xp"] = Weapons.calculate_item_xp_requirement(item)

        if item["lvl"] >= item["max_lvl"]:
            item["xp"] = 0

    @staticmethod
    def gain_item_xp(item, amount):
        if item["lvl"] >= item["max_lvl"]:
            return

        item["xp"] += amount

        while item["xp"] >= item["max_xp"]:
            Weapons.level_up_item(item)






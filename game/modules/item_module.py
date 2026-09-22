from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES, NODE_POOLS
from data.affix_data import ALL_AFFIXES
from systems.items.item_scaling import get_item_level_multiplier

class Item:
    def __init__(self):

        self.id = None
        self.name = ""
        self.type = ""
        self.rarity = None
        self.base_stats = {}
        self.item_lvl = 1
        self.xp = 0
        self.max_xp = 100
        self.lvl = 0
        self.max_lvl = 10
        self.skill_points = 0
        self.skill_tree = {}
        self.unlocked_abilities = []
        self.affixes = []
        self.skill_tags = []

    # def get_species_damage_bonus(self, species):
    #     bonus_dmg = 0
    #
    #     for node in self.skill_tree["nodes"].values():
    #         if node["points"] > 0:
    #
    #             node_pool = NODE_POOLS[node["node_rarity"]]
    #             node_data = node_pool[node["node_id"]]
    #
    #             if species in node_data.damage_modifiers:
    #                 bonus_dmg += node_data.damage_modifiers[species] * node["points"]
    #
    #     return bonus_dmg

    def has_node(self, node_id):
        for node in self.skill_tree["nodes"].values():
            if node["node_id"] == node_id and node["points"] > 0:
                return True

        return False

    def unlock_ability(self, ability_id):
        if ability_id not in self.unlocked_abilities:
            self.unlocked_abilities.append(ability_id)

    @staticmethod
    def skill_tree_bonus(item, stat):
        nodes = item.skill_tree["nodes"].values()

        total = 0

        for node in nodes:

            if node.get("node_type") == "capstone":
                rarity = node["capstone_rarity"]
                node_data = CAPSTONE_NODES[rarity][node["node_id"]]
            else:
                node_pool = NODE_POOLS[node["node_rarity"]]
                node_data = node_pool[node["node_id"]]

            stat_value = node_data.stats.get(stat, 0)
            total += stat_value * node["points"]

        return total

    @staticmethod
    def skill_tree_stats(item):
        stats = []

        nodes = item.skill_tree["nodes"].values()

        for node in nodes:
            if node["points"] <= 0:
                continue

        if node.get("node_type") == "capstone":
            rarity = node["capstone_rarity"]
            node_data = CAPSTONE_NODES[rarity][node["node_id"]]
        else:
            node_data = COMMON_NODES[node["node_id"]]

        for stat in node_data.stats:
            if stat not in stats:
                stats.append(stat)

        return stats

    @staticmethod
    def affix_base_total(item, stat):
        total = item.base_stats.get(stat, 0)

        for affix_id in item.affixes:
            affix_data = ALL_AFFIXES.get(affix_id)
            base_value = affix_data.affix_stats.get(stat, 0)
            multiplier = get_item_level_multiplier(item.item_lvl, affix_data.rarity)
            scaled_value = round(base_value * multiplier)
            total += scaled_value

        return total

    @staticmethod
    def total_bonus(item, stat):
        if not item:
            return 0

        total = Item.affix_base_total(item, stat)
        total += Item.skill_tree_bonus(item, stat)

        return total

    @staticmethod
    def level_up_item(item):
        item.xp -= item.max_xp
        item.lvl += 1
        item.skill_points += 1
        if item.type == "weapon":
            item.max_xp = item.calculate_item_xp_requirement()

        if item.lvl >= item.max_lvl:
            item.xp = 0

    @staticmethod
    def gain_item_xp(item, amount):
        if item.lvl >= item.max_lvl:
            return

        item.xp += amount

        while item.xp >= item.max_xp:
            Item.level_up_item(item)

    def get_xp_percentage(self):
        percentage = round((self.xp / self.max_xp) * 100)

        return percentage


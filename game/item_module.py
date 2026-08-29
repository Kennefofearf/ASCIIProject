from data.skill_node_data import COMMON_NODES, CAPSTONE_NODES
from data.affix_data import GREEN_AFFIXES


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
                node_data = COMMON_NODES[node["node_id"]]

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
            affix_data = GREEN_AFFIXES.get(affix_id, {})
            total += affix_data.affix_stats.get(stat, 0)

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


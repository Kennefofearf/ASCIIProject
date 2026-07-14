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

    def skill_tree_bonus(self, stats):
        total = 0
        for node in self.skill_tree:
            if node.stats == stats:
                total += node.bonus()
        return total

    def total_bonus(self, stat):
        return (
            self.base_stats(stat)
            + self.affix_stats(stat)
            + self.skill_tree_bonus(stat)
        )

    def calculate_item_xp_requirement(self, item):
        if item is None:
            return 0

        average_attack_cooldown = 1.0

        weapon_speed = item["attack_cooldown"]

        xp_requirement = (average_attack_cooldown / weapon_speed) * 100

        return xp_requirement

    def level_up_item(self, item):
        item["xp"] -= item["max_xp"]
        item["lvl"] += 1
        item["skill_points"] += 1
        item["max_xp"] = self.calculate_item_xp_requirement(item)

        if item["lvl"] >= item["max_lvl"]:
            item["xp"] = 0

    def gain_item_xp(self, item, amount):
        if item["lvl"] >= item["max_level"]:
            return

        item["xp"] += amount

        while item["xp"] >= item["max_xp"]:
            self.level_up_item(item)






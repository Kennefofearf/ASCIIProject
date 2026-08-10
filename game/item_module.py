class Item:

    def __init__(self, id, name, type, rarity, base_stats, attack_cooldown, item_lvl, xp, max_xp, lvl, max_lvl,
                 skill_points, abilities, affixes, tags):
        self.id = id
        self.name = name
        self.type = type
        self.rarity = rarity
        self.base_stats = base_stats
        self.attack_cooldown = attack_cooldown
        self.item_lvl = item_lvl
        self.xp = xp
        self.max_xp = max_xp
        self.lvl = lvl
        self.max_lvl = max_lvl
        self.skill_points = skill_points
        self.abilities = []
        self.affixes = {}
        self.tags = []
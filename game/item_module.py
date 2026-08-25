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


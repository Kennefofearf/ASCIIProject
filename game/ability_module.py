class Ability:
    def __init__(self, ability_id, name, tooltip, cooldown, range, target_type, effects):

        self.ability_id = ability_id
        self.name = name
        self.tooltip = tooltip
        self.cooldown = cooldown
        self.range = range
        self.target_type = target_type
        self.effects = effects
class Weapon_Abilities:

    def __init__(self, name, tooltip, points_spent, max_points, gains_per_point, a_range, target):
        self.name = name
        self.tooltip = tooltip
        self.cooldown = 0
        self.buff = None
        self.debuff = None
        self.damage = None
        self.a_range = a_range
        self.target = target
        self.effect = None
        self.points_spent = points_spent
        self.max_points = max_points
        self.gains_per_point = gains_per_point

    @property
    def name(self):
        return f"{self.name}"

    def tooltip(self):
        return f"{self.name}"

    def damage(self):
        return self.damage

    def bonus(self):
        return self.points_spent * self.gains_per_point
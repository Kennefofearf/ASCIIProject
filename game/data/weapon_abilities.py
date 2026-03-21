class Weapon_Abilities:

    def __init__(self, name, tooltip, cooldown, buff, debuff, damage, points_spent, max_points, gains_per_point):
        self.name = name
        self.tooltip = tooltip
        self.cooldown = cooldown
        self.buff = buff
        self.debuff = debuff
        self.damage = damage
        self.points_spent = points_spent
        self.max_points = max_points
        self.gains_per_point = gains_per_point
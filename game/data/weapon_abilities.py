class Weapon_Abilities:

    def __init__(self, name, tooltip, buff, debuff, damage, points_spent, max_points, gains_per_point, effect):
        self.name = name
        self.tooltip = tooltip
        self.cooldown = 0
        self.buff = buff
        self.debuff = debuff
        self.damage = damage
        self.effect = effect
        self.points_spent = points_spent
        self.max_points = max_points
        self.gains_per_point = gains_per_point
        self.last_tick_time = 0

        def bonus(self):
            return self.points_spent * self.gains_per_point
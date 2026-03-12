class Skill:

    def __init__(self, name, tooltip, max_points, points_spent, gains_per_point, effect, stats):
        self.name = name
        self.tooltip = tooltip
        self.points_spent = points_spent
        self.max_points = max_points
        self.gains_per_point = gains_per_point
        self.effect = effect
        self.stats = stats

    def bonus(self):
        return self.points_spent * self.gains_per_point
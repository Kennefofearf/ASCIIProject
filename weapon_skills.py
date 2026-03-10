import random
from player_module import Player

class Skill:

    def __init__(self, name, tooltip, max_points, effect, enabled, points_invested, stat):
        self.name = name
        self.tooltip = tooltip
        self.max_points = max_points
        self.effect = effect
        self.enabled = False
        self.points_invested = points_invested
        self.stat = stat
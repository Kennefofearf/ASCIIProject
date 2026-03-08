import random
from player_module import Player

class Skill:

    def __init__(self, name, tooltip, max_points, effect, enabled):
        self.name = name
        self.tooltip = tooltip
        self.max_points = max_points
        self.effect = effect
        self.enabled = False
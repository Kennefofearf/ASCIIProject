import random
from player_module import Player

class Skill:

    def __init__(self, name, tooltip, max_points, effect, stats):
        self.name = name
        self.tooltip = tooltip
        self.max_points = max_points
        self.effect = effect
        self.stats = stats

        COMMON_SKILLS = {
            "Sharper Edge": {
                "name": "Sharper Edge",
                "tooltip": "Sharpen your weapon increasing STR by 1 per point.",
                "max_points": 5,
                "effect": None,
                "stats": {"max_hp": 0, "st": 1, "df": 0}
            }
        }
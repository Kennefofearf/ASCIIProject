class Node:
    def __init__(self, name, tooltip, points, max_points, stats, requires, unlocks, skill_tags):

        self.name = name
        self.tooltip = tooltip
        self.points = points
        self.max_points = max_points
        self.stats = stats
        self.requires = requires
        self.unlocks = unlocks
        self.skill_tags = skill_tags
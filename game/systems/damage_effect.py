class DamageEffect:

    def __init__(self, base_dmg, scaling_stat, scaling, dmg_type):
        self.base_dmg = base_dmg
        self.scaling_stat = scaling_stat
        self.scaling = scaling
        self.dmg_type = dmg_type

    def apply(self, user, target):
        stat_value = getattr(user, self.scaling_stat, 0)

        total_dmg = self.base_dmg + (stat_value * self.scaling)
        round(total_dmg)

        if self.dmg_type == "blunt":
            total_dmg = max(0, total_dmg - target.df)

        target.take_dmg(total_dmg)

        return total_dmg


def use_ability(user, target, ability):
    damage = int(user.st * ability["damage"])

    target.take_dmg(max(0, damage - target.df))
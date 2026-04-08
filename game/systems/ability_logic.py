from game.data.weapons_abilities_data import COMMON_WEAPON_ABILITIES

def rebuild_abilities(unit):
    usable = set()

    if unit.weapon:
        for ability_id in unit.weapon.get("abilities", []):
            usable.add(ability_id)

    for ability_id in unit.unlocked_abilties:
        usable.add(ability_id)

    unit.abilities = list(usable)

def use_ability(user, target, ability):
    damage = int(user.st * ability["damage"])
    target.take_dmg(max(0, damage - target.df))
    # if "dot" in ability:
    #     apply_dot(target, ability["dot"])
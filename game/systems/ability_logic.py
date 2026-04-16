from game.data.weapons_abilities_data import COMMON_WEAPON_ABILITIES
from game.systems.effect_logic import apply_effect

def rebuild_abilities(unit):
    usable = set()

    if unit.weapon:
        for ability_id in unit.weapon.get("abilities", []):
            usable.add(ability_id)

    for ability_id in unit.unlocked_abilties:
        usable.add(ability_id)

    unit.abilities = list(usable)

def can_use_ability(user, ability_id, now):
    if ability_id not in user.abilities:
        return False, "Ability no longer equipped..."

    if ability_id in user.cooldowns and now < user.cooldowns[ability_id]:
        return False, "That ability is on cooldown."

    return True, ""

def in_range(user, target, ability_data):
    uy, ux = user.position
    ty, tx = target.position
    dist = abs(uy - ty) + abs(ux - tx)
    return dist <= ability_data["range"]

def calculate_ability_damage(user, target, ability_data):
    stat_name = ability_data.get("scaling_stat", "st")
    power = ability_data.get("power", 1.0)

    attack_value = getattr(user, stat_name, 0)
    raw = int(attack_value * power)

    if ability_data.get("damage_type") == "physical":
        return max(0, raw - target.df)

    return raw

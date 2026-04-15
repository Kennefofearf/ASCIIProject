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

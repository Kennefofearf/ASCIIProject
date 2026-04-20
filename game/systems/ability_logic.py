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

def use_ability(user, target, ability_id, now, combat_log=None):
    ability = COMMON_WEAPON_ABILITIES[ability_id]

    ok, reason = can_use_ability(user, ability_id, now)
    if not ok:
        return False, reason

    if ability["target"] == "enemy":
        if target is None or not target.alive:
            return False, "Invalid target."

        if not in_range(user, target, ability):
            return False, "Target out of range."

    if ability["class"] == "attack":
        dmg = calculate_ability_damage(user, target, ability)
        target.take_dmg(dmg)

        if combat_log is not None:
            combat_log.append(f"{user.name} uses {ability['name']} on {target.name} for {dmg} damage.")

        for effect in ability.get("on_hit_effects", []):
            apply_effect(target, effect, now)
            if combat_log is not None:
                combat_log.append(f"{target.name} is afflicted with {effect['effect_id']}")

    user.cooldowns[ability_id] = now + ability["cooldown"]
    return True, "ok"
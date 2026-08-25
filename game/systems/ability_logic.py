from data.weapons_abilities_data import COMMON_WEAPON_ABILITIES

def rebuild_abilities(unit):
    usable = set()

    if unit.weapon:
        for ability_id in unit.weapon.get("abilities", []):
            usable.add(ability_id)

    for ability_id in unit.unlocked_abilties:
        usable.add(ability_id)

    unit.abilities = list(usable)

def can_use_ability(user, ability_id, now):
    if not user.weapon:
        return False, "Required weapon not equipped..."

    if ability_id not in user.ability_slots.values():
        return False, "Ability not equipped..."

    if ability_id in user.cooldowns and now < user.cooldowns[ability_id]:
        return False, "That ability is on cooldown."

    return True, ""

def in_range(user, target, ability_data):
    uy, ux = user.position
    ty, tx = target.position
    dist = abs(uy - ty) + abs(ux - tx)
    return dist <= ability_data.range

def calculate_ability_damage(user, target, ability_data):
    stat_name = ability_data.get("scaling_stat", "st")
    power = ability_data.get("power", 1.0)

    attack_value = getattr(user, stat_name, 0)
    raw = int(attack_value * power)

    if ability_data.get("damage_type") == "physical":
        return max(0, raw - target.df)

    return raw


def use_ability(user, target, ability_id, now, combat_messages=None):
    ability = COMMON_WEAPON_ABILITIES[ability_id]

    ok, reason = can_use_ability(user, ability_id, now)
    if not ok:
        return False, reason

    if ability.target_type == "enemy":
        if target is None or not target.alive:
            return False, combat_messages.append("Invalid target.", 2)

        if not in_range(user, target, ability):
            return False, combat_messages.append("Target out of range.", 2)

    # if ability["class"] == "attack":
    #     dmg = calculate_ability_damage(user, target, ability)
    #     target.take_dmg(dmg)

    for effect in ability.effects:
        result = effect.apply(user, target)

        if combat_messages is not None:
            combat_messages.append([(f"{user.name} ", 2), ("uses ", 0), (f"{ability.name} ", 2), ("on ", 0),
                                    (f"{target.name} ", 1), ("for ", 0), (f"{result} ", 2), ("damage!", 0)])
            # if combat_log is not None:
            #     combat_log.append(f"{target.name} is afflicted with {effect['effect_id']}")

    user.cooldowns[ability_id] = now + ability.cooldown

    return True, "ok"


def apply_effect(target, effect_data, now):
    target.active_effects.append({
        "effect_id": effect_data["effect_id"],
        "duration": effect_data["duration"],
        "tick_rate": effect_data.get("tick_rate", 1),
        "value": effect_data.get("value", 0),
        "started_at": now,
        "last_tick": now
    })

def process_effects(unit, now, combat_log=None):
    remaining = []

    for effect in unit.active_effects:
        effect_id = effect["effect_id"]

        if effect_id == "poison":
            if now - effect["last_tick"] >= effect["tick_rate"]:
                dmg = effect["value"]
                unit.take_dmg(dmg)
                effect["last_tick"] = now

                if combat_log is not None:
                    combat_log.append(f"{unit.name} ticks for {dmg} damage")

        expired = (now - effect["started_at"]) >= effect["duration"]

        if not expired and unit.alive:
            remaining.append(effect)
        elif combat_log is not None:
            combat_log.append(f"{effect_id} has dropped from {unit.name}")

    unit.active_effects = remaining
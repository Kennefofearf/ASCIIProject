def apply_effect(target, effect_data, now):
    target.active_effects.append({
        "effect_id": effect_data["effect_id"],
        "duration": effect_data["duration"],
        "tick_rate": effect_data.get("tick_rate", 1),
        "value": effect_data.get("value", 0),
        "started_at": now,
        "last_tick": now
    })
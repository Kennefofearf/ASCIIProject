COMMON_WEAPON_ABILITIES = {
    "gash": {
        "name": "Gash",
        "class": "attack",
        "tooltip": "Give the target a deep cut that inflicts 10 damage over 5 seconds.",
        "cooldown": 8,
        "buff": None,
        "debuff": None,
        "damage": 3,
        "damage_type": "physical",
        "on_hit_effects": "bleed",
        "range": 1,
        "target": "enemy",
        "effect": [
            {
                "EFFECT": "bleed",
                "duration": 5,
                "value": 2
            }
        ],
        "scaling_stat": "st"
    },
    "bash": {
        "name": "Bash",
        "tooltip": "Hit the target with the hilt of your weapon for X damage.",
        "cooldown": 10,
        "buff": None,
        "debuff": None,
        "damage": 10,
        "range": 1,
        "target": "enemy",
        "effect": None
    }
}

COMMON_WEAPON_ABILITIES = {
    "Gash": {
        "name": "Gash",
        "tooltip": "Give the target a deep cut that inflicts 10 damage over 5 seconds.",
        "cooldown": 8,
        "buff": None,
        "debuff": None,
        "damage": 3,
        "range": 1,
        "target": "enemy",
        "effect": [
            {
                "type": "bleed",
                "damage": 2,
                "duration": 5,
                "interval": 1
            }
        ]
    },
    "Bash": {
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

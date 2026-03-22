import time

now = time.time()

COMMON_WEAPON_ABILITIES = {
        "Gash": {
        "name": "Gash",
        "tooltip": "Give the target a deep cut that inflicts 10 damage over 5 seconds.",
        "cooldown": 8,
        "buff": None,
        "debuff": None,
        "damage": 3,
        "effect": [
                {
                "type": "bleed",
                "damage": 2,
                "duration": 5,
                "interval": 1
                }
        ]
    }
}
COMMON_NODES = {
            "sharper_edge": {
                "name": "Sharper Edge",
                "tooltip": "Sharpen your weapon increasing STR by 1.",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 0, "st": 1, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "full_body_callus": {
                "name": "Full Body Callus",
                "tooltip": "The skin on your body thickens raising DEF by 1.",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 0, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["armor"]
            },
            "pain_tolerance": {
                "name": "Pain Tolerance",
                "tooltip": "Ignoring pain becomes easier. Raises your Max HP by 3.",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 3, "st": 0, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "cautious": {
                "name": "Cautious",
                "tooltip": "You always think before acting. Raises your Max HP by 2 & DEF by 1.",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 2, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "reckless": {
                "name": "Reckless",
                "tooltip": "You love to charge in without a plan. Raises STR by 3 & decreases DEF by 1.",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 0, "st": 3, "df": -1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "confidence": {
                "name": "Confidence",
                "tooltip": "You believe in your ability to stand up to your opponents. HP +5 DEF +1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 5, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "frail": {
                "name": "Frail",
                "tooltip": "Your body gets weaker. HP -5 STR -1 DEF -1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -5, "st": -1, "df": -1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "turtle instincts": {
                "name": "Turtle Instincts",
                "tooltip": "You prioritize sheilding yourself above all else. HP - 15 STR -3 DEF +3",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -15, "st": -3, "df": 5},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "ability_bash": {
                "name": "Bash",
                "tooltip": "Hit the target with the hilt of your weapon for X damage.",
                "points": 0,
                "max_points": 5,
                "stats": {},
                "requires": [],
                "unlocks": ["bash"],
                "skill_tags": ["weapon"]
            },
            "ability_gash": {
                "name": "Gash",
                "tooltip": "Give the target a deep cut that inflicts 10 damage over 5 seconds.",
                "points": 0,
                "max_points": 3,
                "stats": {},
                "requires": [],
                "unlocks": ["gash"],
                "skill_tags": ["weapon"]
            }
        }
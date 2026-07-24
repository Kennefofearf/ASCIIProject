COMMON_NODES = {
            "sharper_edge": {
                "name": "Sharper Edge",
                "tooltip": "Sharpen your weapon.\n\nSTR +1",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 0, "st": 1, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "full_body_callus": {
                "name": "Full Body Callus",
                "tooltip": "The skin on your body thickens.\n\nDEF +1",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 0, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["armor"]
            },
            "pain_tolerance": {
                "name": "Pain Tolerance",
                "tooltip": "Ignoring pain becomes easier.\n\nHP +3",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 3, "st": 0, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "cautious": {
                "name": "Cautious",
                "tooltip": "You always think before acting.\n\nHP +2\nDEF +1",
                "points": 0,
                "max_points": 5,
                "stats": {"max_hp": 2, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "reckless": {
                "name": "Reckless",
                "tooltip": "You love to charge in without a plan.\n\nSTR +3\nDEF -1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 0, "st": 3, "df": -1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon"]
            },
            "confidence": {
                "name": "Confidence",
                "tooltip": "You believe in your ability to stand up to your opponents.\n\nHP +5\nDEF +1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 5, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "frail": {
                "name": "Frail",
                "tooltip": "Your body gets weaker.\n\nHP -5\nSTR -1\nDEF -1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -5, "st": -1, "df": -1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "turtle instincts": {
                "name": "Turtle Instincts",
                "tooltip": "You prioritize shielding yourself above all else.\n\nHP -15\nSTR -3\nDEF +5",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -15, "st": -3, "df": 5},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "block training": {
                "name": "Block Training",
                "tooltip": "You practice blocking blows from various angles.\n\nDEF +1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 0, "st": 0, "df": 1},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "weight lifting": {
                "name": "Weight Lifting",
                "tooltip": "Lifting weights helps you build muscle.\n\nSTR +1",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 0, "st": 1, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "illness": {
                "name": "Illness",
                "tooltip": "The equipment's aura makes you nauseous.\n\nHP -10",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -10, "st": 0, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "handicap": {
                "name": "Handicap",
                "tooltip": "You're very confident in yourself.\n\nHP -10\nSTR -3\nDEF -3",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": -10, "st": -3, "df": -3},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "goof off": {
                "name": "Goof Off",
                "tooltip": "You love wasting time.\n\nHP +0\nSTR +0\nDEF +0",
                "points": 0,
                "max_points": 3,
                "stats": {"max_hp": 0, "st": 0, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
            "ability_bash": {
                "name": "Bash",
                "tooltip": "Hit the target with the hilt of your weapon.\n\n6-8 damage",
                "points": 0,
                "max_points": 5,
                "stats": {},
                "requires": [],
                "unlocks": ["bash"],
                "skill_tags": ["weapon"]
            },
            "ability_gash": {
                "name": "Gash",
                "tooltip": "Give the target a deep cut.\n\n10 damage over 5 seconds",
                "points": 0,
                "max_points": 3,
                "stats": {},
                "requires": [],
                "unlocks": ["gash"],
                "skill_tags": ["weapon"]
            }
        }

CAPSTONE_NODES = {
    "white": {
            "constitution boost": {
                "name": "Constitution Boost",
                "tooltip": "Your physical health inspires others.\n\nHP +30",
                "points": 0,
                "max_points": 1,
                "stats": {"max_hp": 30, "st": 0, "df": 0},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            }
    },
    "green": {
            "level up": {
                "name": "Level Up",
                "tooltip": "You level up in a more traditional way.\n\nHP +10\nSTR +5\nDEF +5",
                "points": 0,
                "max_points": 1,
                "stats": {"max_hp": 10, "st": 5, "df": 5},
                "requires": [],
                "unlocks": [],
                "skill_tags": ["weapon", "armor"]
            },
    }
}




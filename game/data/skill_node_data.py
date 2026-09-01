from skill_node_module import Node

STAT_NAMES = {
    "max_hp": "HP",
    "st": "STR",
    "df": "DEF",
    "mp": "MGP",
    "ev": "EVA",
    "cr": "CRT",
    "cd": "CRD",
    "hp_rr": "HRR",
    "hp_ra": "HRA"
}

COMMON_NODES = {
            "sharper_edge": Node(
                name="Sharper Edge",
                tooltip="Sharpen your weapon.",
                points=0,
                max_points=5,
                stats={"max_hp": 0, "st": 1, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "full_body_callus": Node(
                name="Full Body Callus",
                tooltip="The skin on your body thickens.",
                points=0,
                max_points=5,
                stats={"max_hp": 0, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["armor"]
            ),
            "pain_tolerance": Node(
                name="Pain Tolerance",
                tooltip="Ignoring pain becomes easier.",
                points=0,
                max_points=5,
                stats={"max_hp": 3, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "cautious": Node(
                name="Cautious",
                tooltip="You always think before acting.",
                points=0,
                max_points=5,
                stats={"max_hp": 2, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "reckless": Node(
                name="Reckless",
                tooltip="You love to charge in without a plan.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 3, "df": -1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon"]
            ),
            "confidence": Node(
                name="Confidence",
                tooltip="You believe in your ability to stand up to your opponents.",
                points=0,
                max_points=3,
                stats={"max_hp": 5, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "frail": Node(
                name="Frail",
                tooltip="Your body gets weaker.",
                points=0,
                max_points=3,
                stats={"max_hp": -5, "st": -1, "df": -1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "turtle instincts": Node(
                name="Turtle Instincts",
                tooltip="You prioritize shielding yourself above all else.",
                points=0,
                max_points=3,
                stats={"max_hp": -15, "st": -3, "df": 5, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "block training": Node(
                name="Block Training",
                tooltip="You practice blocking blows from various angles.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 1, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "weight lifting": Node(
                name="Weight Lifting",
                tooltip="Lifting weights helps you build muscle.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 1, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "illness": Node(
                name="Illness",
                tooltip="The equipment's aura makes you nauseous.",
                points=0,
                max_points=3,
                stats={"max_hp": -10, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "handicap": Node(
                name="Handicap",
                tooltip="You're very confident in yourself.",
                points=0,
                max_points=3,
                stats={"max_hp": -10, "st": -3, "df": -3, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "goof off": Node(
                name="Goof Off",
                tooltip="You love wasting time.",
                points=0,
                max_points=3,
                stats={"max_hp": 0, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
            "bash": Node(
                name="Bash",
                tooltip="Unlocks Bash",
                points=0,
                max_points=1,
                stats={},
                requires=[],
                unlocks=["bash"],
                skill_tags=["weapon"]
            ),
            "gash": Node(
                name="Gash",
                tooltip="Give the target a deep cut. Dealing 10 damage over 5 seconds",
                points=0,
                max_points=3,
                stats={},
                requires=[],
                unlocks=["gash"],
                skill_tags=["weapon"]
            )
        }

BLUE_NODES = {
            "fluid swings": Node(
                name="Fluid Swings",
                tooltip="Your swings are practiced and professional.",
                points=0,
                max_points=3,
                stats={"st": 3},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

YELLOW_NODES = {
            "evasive maneuvers": Node(
                name="Evasive Maneuvers",
                tooltip="Your agility improves.",
                points=0,
                max_points=3,
                stats={"ev": 1},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

PURPLE_NODES = {
            "captain's vigor": Node(
                name="Captain's Vigor",
                tooltip="Your vigor matches that of a captain in an army.",
                points=0,
                max_points=3,
                stats={"max_hp": 150, "st": 8, "df": 4},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
}

CAPSTONE_NODES = {
    "white": {
            "constitution boost": Node(
                name="Constitution Boost",
                tooltip="Your physical health inspires others.",
                points=0,
                max_points=1,
                stats={"max_hp": 30, "st": 0, "df": 0, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            )
    },
    "green": {
            "level up": Node(
                name="Level Up",
                tooltip="You level up in a more traditional way.",
                points=0,
                max_points=1,
                stats={"max_hp": 10, "st": 5, "df": 5, "mp": 0, "ev": 0, "cr": 0, "cd": 0, "hp_rr": 0, "hp_ra": 0},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "blue": {
            "troll dna": Node(
                name="Troll DNA",
                tooltip="Your regeneration is not natural.",
                points=0,
                max_points=1,
                stats={"hp_rr": 2.0, "hp_ra": 15},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "yellow": {
            "curse of dwarfism": Node(
                name="Curse of Dwarfism",
                tooltip="You shrink to a smaller size affecting HP and EVA.",
                points=0,
                max_points=1,
                stats={"max_hp": -100, "ev": 20},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    },
    "purple": {
            "effortless destruction": Node(
                name="Effortless Destruction",
                tooltip="Your blows can be devastating without you breaking a sweat.",
                points=0,
                max_points=1,
                stats={"cr": 30, "cd": 25},
                requires=[],
                unlocks=[],
                skill_tags=["weapon", "armor"]
            ),
    }
}

NODE_POOLS = {"white": COMMON_NODES, "green": COMMON_NODES, "blue": BLUE_NODES, "yellow": YELLOW_NODES,
              "purple": PURPLE_NODES}




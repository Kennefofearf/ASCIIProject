RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]

# TIERS = {
#     "white": range(9, 16),
#     "green": range(17, 24),
#     "blue": range(25, 32),
#     "yellow": range(33, 40),
#     "purple": range(41, 48)
# }

LAYOUTS = {
    "white": [
        {
            "slots": [
                (5, 9), (5, 17), (5, 25),
                (12, 9), (12, 17), (12, 25),
                None,    (19, 17), None
            ],
            "capstone_slot": 7,
            "connections": [
                (0, 3),
                (1, 4),
                (2, 5),
                (3, 4),
                (4, 1),
                (4, 3),
                (4, 5),
                (4, 7)
            ],
            "entry_slots": [
                2
            ],
            "exit_slots": [
                0
            ],
        },
        {
            "slots": [
                (5, 9), None, None,
                (12, 9), (12, 17), (12, 25),
                None, (19, 17), None
            ],
            "capstone_slot": 7,
            "connections": [
                (0, 3),
                (3, 4),
                (4, 5),
                (4, 7)
            ],
            "entry_slots": [
                0
            ],
            "exit_slots": [
                0
            ],
        },
    ],

    "green": [
        {
            "slots": [
                (26, 9), (26, 17), (26, 25),
                (33, 9), (33, 17), (33, 25),
                None,    (40, 17), None
            ],
            "capstone_slot": 7,
            "connections": [
                (0, 3),
                (1, 4),
                (2, 5),
                (3, 4),
                (4, 1),
                (4, 3),
                (4, 5),
                (4, 7)
            ],
            "entry_slots": [
                2
            ],
            "exit_slots": [
                0
            ],
        },
        {
            "slots": [
                (26, 9), (26, 17), None,
                (33, 9), None, None,
                (40, 9), (40, 17), None
            ],
            "capstone_slot": 7,
            "connections": [
                (0, 1),
                (0, 3),
                (1, 0),
                (3, 0),
                (3, 6),
                (6, 3),
                (6, 7),
                (7, 6)
            ],
            "entry_slots": [
                1
            ],
            "exit_slots": [
                1
            ],
        },
    ],
}


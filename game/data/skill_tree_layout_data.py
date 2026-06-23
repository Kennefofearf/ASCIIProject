RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]

LAYOUTS = {
    "white": [
        {
        "slots": [
            (50, 7), (50, 19), (50, 31),
            (45, 7), (45, 19), (45, 31),
            None,    (40, 19), None
        ],
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
            (0, 1, 2)
        ],
        "exit_slots": [
            7
        ]
        }
    ],
    "white": [
        {
        "slots": [
            (50, 7), None, None,
            (45, 7), (45, 19), (45, 31),
            None, (40, 19), None
        ],
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
            7
        ]
        }
    ],

    "green": [
        {
        "slots": [
            (35, 7), (35, 19), (35, 31),
            (30, 7), (30, 19), (30, 31),
            None,    (25, 19), None
        ],
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
            (0, 1, 2)
        ],
        "exit_slots": [
            7
        ]
        }
    ],
    "green": [
        {
        "slots": [
            (35, 7), (35, 19), None,
            (30, 7), None, None,
            (25, 7), (25, 19), None
        ],
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
            (0, 1)
        ],
        "exit_slots": [
            (6, 7)
        ]
        }
    ],
}
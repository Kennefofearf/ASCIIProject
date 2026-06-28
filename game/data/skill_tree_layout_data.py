RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]

LAYOUTS = {
    "white": [
        {
        "slots": [
            (50, 1), (50, 8), (50, 15),
            (45, 1), (45, 8), (45, 15),
            None,    (40, 8), None
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
            2
        ],
        "exit_slots": [
            0
        ]
        }
    ],
    "white": [
        {
        "slots": [
            (50, 1), None, None,
            (45, 1), (45, 8), (45, 15),
            None, (40, 8), None
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
            0
        ]
        }
    ],

    "green": [
        {
        "slots": [
            (35, 1), (35, 8), (35, 15),
            (30, 1), (30, 8), (30, 15),
            None,    (25, 8), None
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
            2
        ],
        "exit_slots": [
            0
        ]
        }
    ],
    "green": [
        {
        "slots": [
            (35, 1), (35, 8), None,
            (30, 1), None, None,
            (25, 1), (25, 8), None
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
            1
        ],
        "exit_slots": [
            1
        ]
        }
    ],
}
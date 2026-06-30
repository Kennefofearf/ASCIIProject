RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]

LAYOUTS = {
    "white": [
        {
        "slots": [
            (40, 1), (40, 9), (40, 17),
            (33, 1), (33, 9), (33, 17),
            None,    (26, 9), None
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
            (40, 1), None, None,
            (33, 1), (33, 9), (33, 17),
            None, (26, 9), None
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
            (19, 1), (19, 9), (19, 17),
            (12, 1), (12, 9), (12, 17),
            None,    (5, 9), None
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
            (19, 1), (19, 9), None,
            (12, 1), None, None,
            (5, 1), (5, 9), None
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
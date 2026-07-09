RARITY_ORDER = ["white", "green", "blue", "yellow", "purple"]

LAYOUTS = {
    "white": [
        {
            "slots": [
                (5, 1), (5, 9), (5, 17),
                (12, 1), (12, 9), (12, 17),
                None,    (19, 9), None
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
                (5, 1), None, None,
                (12, 1), (12, 9), (12, 17),
                None, (19, 9), None
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
                (26, 1), (26, 9), (26, 17),
                (33, 1), (33, 9), (33, 17),
                None,    (40, 9), None
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
                (26, 1), (26, 9), None,
                (33, 1), None, None,
                (40, 1), (40, 9), None
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


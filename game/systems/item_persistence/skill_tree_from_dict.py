def skill_tree_from_dict(data):
    nodes = {}
    capstones = {}
    slot_rarities = {}

    for key, node in data["nodes"].items():
        nodes[int(key)] = node

    for key, capstone_rarity in data["layout"]["capstones"].items():
        capstones[int(key)] = capstone_rarity

    for key, rarity in data["layout"]["slot_rarities"].items():
        slot_rarities[int(key)] = rarity

    data["nodes"] = nodes
    data["layout"]["capstones"] = capstones
    data["layout"]["slot_rarities"] = slot_rarities

    return data

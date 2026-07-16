def get_rarity_color(item):
    return get_color_from_rarity(item["rarity"])


def get_color_from_rarity(rarity):
    if rarity == "white":
        return 0
    elif rarity == "green":
        return 3
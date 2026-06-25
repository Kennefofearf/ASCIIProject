def get_rarity_color(item):
    rarity = item.get("rarity")
    item_level = item.get("item_level")

    # item level determines possible rarity

    if rarity == "white":
        return 0
    elif rarity == "green" and item_level >= 5:
        return 3

    return 0
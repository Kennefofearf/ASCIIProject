def player_to_dict(player):
    saved_char = {
        "name": player.name,
        "base_max_hp": player.base_max_hp,
        "hp": player.hp,
        "base_st": player.base_st,
        "base_df": player.base_df,
        "base_ac": player.base_ac,
        "base_mp": player.base_mp,
        "base_evasion": player.base_evasion,
        "base_crit_rate": player.base_crit_rate,
        "base_crit_dmg": player.base_crit_dmg,
        "base_hp_rr": player.base_hp_rr,
        "base_hp_ra": player.base_hp_ra,
        "req_xp": player.req_xp,
        "total_req_xp": player.total_req_xp,
        "lvl": player.lvl,
        "position": player.position
    }

    return saved_char

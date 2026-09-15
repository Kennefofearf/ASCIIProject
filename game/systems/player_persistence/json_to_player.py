from modules.player_module import Player


def json_to_player(data):
    player = Player(data['name'])

    player.base_max_hp = data["base_max_hp"]
    player.hp = data["hp"]
    player.base_st = data["base_st"]
    player.base_df = data["base_df"]
    player.base_ac = data["base_ac"]
    player.base_mp = data["base_mp"]
    player.base_evasion = data["base_evasion"]
    player.base_crit_rate = data["base_crit_rate"]
    player.base_crit_dmg = data["base_crit_dmg"]
    player.base_hp_rr = data["base_hp_rr"]
    player.base_hp_ra = data["base_hp_ra"]

    player.req_xp = data["req_xp"]
    player.total_req_xp = data["total_req_xp"]
    player.lvl = data["lvl"]
    player.position = data["position"]

    return player

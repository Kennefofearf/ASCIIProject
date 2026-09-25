from UI.enemy_window import create_enemy_window
from UI.combat_log import create_combat_log_windows
from UI.player_window import create_player_window, create_gear_progress_window
from UI.action_bar import create_action_bar


def create_game_windows(stdscr):
    stdscr.clear()

    enemy_window = create_enemy_window(stdscr)
    outer, inner, outer_h, outer_w = create_combat_log_windows(stdscr)
    player_window = create_player_window(stdscr)
    gear_progress_window = create_gear_progress_window(stdscr)
    action_bar = create_action_bar(stdscr)

    log_height = inner.getmaxyx()[0]

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))

    return (
        enemy_window,
        outer,
        inner,
        outer_h,
        outer_w,
        player_window,
        gear_progress_window,
        action_bar,
        log_height
    )

import curses


def create_player_window(stdscr):
    screen_y, screen_x = stdscr.getmaxyx()

    playerwin_h, playerwin_w = 10, 20

    player_window = curses.newwin(playerwin_h, playerwin_w, int(screen_y * 0.73), int(screen_x * 0.01))

    return player_window


def draw_player_window(player_window, player):
    player_window.addstr(1, 2, f"{player.name}  Level: {player.lvl}")

    if player.weapon:
        player_window.addstr(3, 1, f"DMG: {player.weapon.min_dmg + player.st} - "
                                   f"{player.weapon.max_dmg + player.st}")
    else:
        player_window.addstr(3, 1, f"DMG: {player.st} - {player.st}")

    player_window.addstr(4, 1, f" HP:   {player.hp} / {player.max_hp}")
    player_window.addstr(5, 1, f"STR:   {player.st}")
    player_window.addstr(6, 1, f"DEF:   {player.df} (AC: {player.ac})")
    player_window.addstr(7, 1, f" XP: {player.total_req_xp - player.req_xp} / {player.total_req_xp}")
    player_window.addstr(8, 1, f"[")
    player_window.addstr(8, 2, f"{player.xp_bar_text:<10}")
    player_window.addstr(8, 12, f"]")
    player_window.refresh()
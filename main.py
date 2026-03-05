import curses
from curses import wrapper
from player_module import Player
from monster_module import GiantAnt

enemies = []

for enemy in range(3):
    e = GiantAnt()
    enemies.append(e)

def mouse_actions(mx, my, bstate, stdscr):
    if bstate & curses.BUTTON1_CLICKED:
        for selected in enemies:
            if (my, mx) == tuple(selected.position) and selected.alive:
                return True, selected
        return True, None
    return False, None

def world_event_logic(player, py, px, player_window, target_window, stdscr):
    ny, nx = player.future_position(py, px)
    if not movement_area(stdscr, ny, nx):
        py = 0
        px = 0

    for e in enemies:
        e.respawn_timer(player)
        if e.alive == False:
            continue

        ey, ex = e.enemy_random_movement()
        ney, nex = e.future_position(ey, ex)

        if not movement_area(stdscr, ney, nex):
            ey = 0
            ex = 0

        elif (ney, nex) == tuple(player.position):
            ey = 0
            ex = 0
            player.take_dmg(max(0, e.st - player.df))
            e.take_dmg(max(0, player.st - e.df))
            player_window.erase()
            player_window.refresh()

        elif (ny, nx) == tuple(e.position):
            py = 0
            px = 0
            e.take_dmg(max(0, player.st - e.df))
            player.take_dmg(max(0, e.st - player.df))
            target_window.erase()
            target_window.refresh()

        elif (ny, nx) == (ney, nex):
            py = 0
            px = 0

        if not e.alive:
            player.xp_gain(e.xp)
            player_window.erase()
            player_window.refresh()

        e.move(ey, ex)
        stdscr.addch(e.position[0], e.position[1], e.icon)

    player.move(py, px)

def movement_area(win, y, x):
    h, w = win.getmaxyx()
    return 1 <= y <= h - 2 and 1 <= x <= w - 2

def gamestart(stdscr):
    curses.cbreak()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)
    stdscr.timeout(17)

    stdscr.clear()

    player = Player("Koe", "@", 50, 50, 10, 3, 4, 1)
    player.position = [20, 55]

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
    stdscr.refresh()
    targetwin_h, targetwin_w = 10, 20
    playerwin_h, playerwin_w = 10, 20
    target_window = curses.newwin(targetwin_h, targetwin_w, 29, 99)
    player_window = curses.newwin(playerwin_h, playerwin_w, 29, 0)
    dbg = curses.newwin(12, 30, 1, 89)
    selected = None

    prev_positions = []

    while True:
        for y, x in prev_positions:
            stdscr.addch(y, x, ord(" "))

        prev_positions = []

        target_window.box()
        player_window.box()
        dbg.box()

        player.player_spawn(stdscr, prev_positions, player)
        for enemy in enemies:
            if enemy.alive:
                stdscr.addch(enemy.position[0], enemy.position[1], enemy.icon)
                prev_positions.append(tuple(enemy.position))

        stdscr.refresh()

        if selected and selected.alive:
            target_window.addstr(1, 1, f"   {selected.name}")
            target_window.addstr(3, 1, f" HP:   {selected.max_hp} / {selected.hp}")
            target_window.addstr(5, 1, f"STR:   {selected.st}")
            target_window.addstr(7, 1, f"DEF:   {selected.df}")
            target_window.refresh()
        else:
            target_window.erase()
            target_window.box()
            target_window.refresh()

        player_window.addstr(1, 1, f"       {player.name}")
        player_window.addstr(2, 1, f"Lvl:   {player.lvl}")
        player_window.addstr(3, 1, f" HP:   {player.max_hp} / {player.hp}")
        player_window.addstr(4, 1, f"STR:   {player.st}")
        player_window.addstr(5, 1, f"DEF:   {player.df}")
        player_window.addstr(6, 1, f"Nxt:   {player.req_xp}")
        player_window.refresh()

        dbg.addstr(1, 1, f"Player: {player.position}")
        dbg.addstr(2, 1, f"eCords: {enemies[0].position}")
        dbg.addstr(3, 1, f"eCords: {e.position}")
        dbg.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()
            clicked, picked = mouse_actions(mx, my, bstate, stdscr)
            if clicked:
                selected = picked

        py, px = player.input_action(key)

        world_event_logic(player, py, px, player_window, target_window, stdscr)
        stdscr.refresh()

wrapper(gamestart)

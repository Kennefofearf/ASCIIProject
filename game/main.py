import curses
import time
from curses import wrapper
from player_module import Player
from monster_module import GiantAnt

enemies = []

for enemy in range(3):
    e = GiantAnt()
    enemies.append(e)

def mouse_actions(mx, my, bstate, player):
    if bstate & curses.BUTTON1_CLICKED:
        for enemy in enemies:
            if (my, mx) == tuple(enemy.position) and enemy.alive:
                player.target = enemy
                return True, enemy
        return True, None
    return False, None

def draw_enemies(stdscr, enemies, selected, prev_positions, hovered):
    for enemy in enemies:
        if not enemy.alive:
            continue

        y, x = enemy.position

        if enemy == selected:
            attr = curses.color_pair(1)
        # elif enemy == hovered:
        #     attr = curses.A_REVERSE
        else:
            attr = curses.A_NORMAL

        stdscr.addch(y, x, enemy.icon, attr)
        prev_positions.append((y, x))

def is_adjacant(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y1 - y2) + abs(x1 - x2) == 1

def player_auto_attack_logic(player, target_window, player_window):
    target = player.target

    if target is None:
        return

    if not target.alive:
        player.target = None
        return

    if is_adjacant(player.position, target.position):
        now = time.time()
        if now - player.last_attack_time >= player.attack_cooldown:
            target.take_dmg(max(0, player._st - target.df))
            target_window.erase()
            target_window.refresh()
            player.last_attack_time = now

        if not target.alive:
            player.xp_gain(target.xp)
            player.target = None
            player_window.erase()
            player_window.refresh()


def e_auto_attack_logic(e, player, player_window):

    for e in enemies:
        if not e.alive:
            continue

        if is_adjacant(e.position, player.position):
            e.is_attacking = True
            now = time.time()
            if now - e.last_attack_time >= e.attack_cooldown:
                player.take_dmg(max(0, e.st - player._df))
                player_window.erase()
                player_window.refresh()
                e.last_attack_time = now

        else:
            e.is_attacking = False

def world_event_logic(player, py, px, player_window, target_window, stdscr):
    ny, nx = player.future_position(py, px)
    if not movement_area(stdscr, ny, nx):
        py = 0
        px = 0

    player_auto_attack_logic(player, target_window, player_window)

    for e in enemies:
        e.respawn_timer(player)
        if e.alive == False:
            continue

        ey, ex = e.enemy_random_movement()
        ney, nex = e.future_position(ey, ex)

        e_auto_attack_logic(e, player, player_window)

        if not movement_area(stdscr, ney, nex):
            ey = 0
            ex = 0

        elif (ney, nex) == tuple(player.position):
            ey = 0
            ex = 0

        elif (ny, nx) == tuple(e.position):
            py = 0
            px = 0

        elif (ny, nx) == (ney, nex):
            py = 0
            px = 0

        e.move(ey, ex)

    player.move(py, px)

def movement_area(win, y, x):
    h, w = win.getmaxyx()
    return 1 <= y <= h - 2 and 1 <= x <= w - 2

def gamestart(stdscr):
    curses.cbreak()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)
    stdscr.timeout(17)
    selected = None
    hovered = None

    stdscr.clear()

    player = Player("Koe", "@", 50, 50, 3, 3, 4, 1)
    player.position = [20, 55]

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
    stdscr.refresh()
    targetwin_h, targetwin_w = 10, 20
    playerwin_h, playerwin_w = 10, 20
    target_window = curses.newwin(targetwin_h, targetwin_w, 29, 99)
    player_window = curses.newwin(playerwin_h, playerwin_w, 29, 0)
    dbg = curses.newwin(12, 30, 1, 89)

    prev_positions = []

    while True:
        #time.sleep(0.5)
        #time.sleep(2)
        for y, x in prev_positions:
            stdscr.addch(y, x, ord(" "))

        prev_positions = []

        target_window.box()
        player_window.box()
        dbg.box()

        player.player_spawn(stdscr, prev_positions, player)
        draw_enemies(stdscr, enemies, selected, prev_positions, hovered)

        stdscr.refresh()

        if selected and selected.alive:
            target_window.addstr(1, 1, f"   {selected.name}")
            target_window.addstr(3, 1, f" HP:   {selected.hp} / {selected.max_hp}")
            target_window.addstr(5, 1, f"STR:   {selected.st}")
            target_window.addstr(7, 1, f"DEF:   {selected.df}")
            target_window.refresh()
        else:
            target_window.erase()
            target_window.box()
            target_window.refresh()

        player_window.addstr(1, 1, f"       {player.name}")
        player_window.addstr(2, 1, f"Lvl:   {player.lvl}")
        player_window.addstr(3, 1, f" HP:   {player._hp} / {player.max_hp}")
        player_window.addstr(4, 1, f"STR:   {player._st}")
        player_window.addstr(5, 1, f"DEF:   {player._df}")
        player_window.addstr(6, 1, f"Nxt:   {player.req_xp}")
        player_window.refresh()

        dbg.addstr(1, 1, f"{player.target}")
        dbg.addstr(2, 1, f"{selected}")
        dbg.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()
            hovered = None
            for enemy in enemies:
                if enemy.alive and (my, mx) == tuple(enemy.position):
                    hovered = enemy
                    break

            clicked, picked = mouse_actions(mx, my, bstate, player)
            if clicked:
                selected = picked
                player.target = picked

        py, px = player.input_action(key)

        world_event_logic(player, py, px, player_window, target_window, stdscr)

        if selected and not selected.alive:
            selected = None

        stdscr.refresh()

wrapper(gamestart)

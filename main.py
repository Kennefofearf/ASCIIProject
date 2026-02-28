import curses
import random
import monster_module
import player_module
from curses import wrapper
from player_module import Player
from monster_module import GiantAnt

enemies = []

for enemy in range(3):
    e = GiantAnt()
    e.position = [random.randint(2, 19), random.randint(2, 99)]
    enemies.append(e)

def mouse_actions(enemy, mx, my, player, bstate, show_target):
    if bstate & curses.BUTTON1_PRESSED:
        if (my, mx) == tuple(enemy.position):
            show_target = True
        else:
            show_target = False
    return show_target

def world_event_logic(player, enemy, py, px, ey, ex, player_window, target_window, stdscr, random_inty, random_intx):
    ny, nx = player.future_position(py, px)
    ney, nex = enemy.future_position(ey, ex)
    if not movement_area(stdscr, ny, nx):
        py = 0
        px = 0

    if enemy.alive:
        if not movement_area(stdscr, ney, nex):
            ey = 0
            ex = 0

        elif (ney, nex) == tuple(player.position):
            ey = 0
            ex = 0
            player.take_dmg(max(0, enemy.st - player.df))
            enemy.take_dmg(max(0, player.st - enemy.df))
            player_window.erase()
            player_window.refresh()

        elif (ny, nx) == tuple(enemy.position):
            py = 0
            px = 0
            enemy.take_dmg(max(0, player.st - enemy.df))
            player.take_dmg(max(0, enemy.st - player.df))
            target_window.erase()
            target_window.refresh()

        elif (ny, nx) == (ney, nex):
            py = 0
            px = 0

    player.move(py, px)
    if enemy.alive:
        enemy.move(ey, ex)
        stdscr.addch(enemy.position[0], enemy.position[1], enemy.icon)

def movement_area(win, y, x):
    h, w = win.getmaxyx()
    return 1 <= y <= h - 2 and 1 <= x <= w - 2

# def player_spawn(stdscr, prev_positions, player):
#     stdscr.addch(player.position[0], player.position[1], player.icon)
#     prev_positions.append(tuple(player.position))

# def monster_spawner(stdscr, prev_positions, enemy):
#     if enemy.alive:
#         movement_area(stdscr, enemy.position[0], enemy.position[1])
#         stdscr.addch(enemy.position[0], enemy.position[1], enemy.icon)
#         prev_positions.append(tuple(enemy.position))


def gamestart(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)
    stdscr.timeout(17)

    stdscr.clear()

    random_inty, random_intx = random.randint(1, 20), random.randint(1, 100)
    # random_movement = random.randint(1, 10)
    # random_direction = random.randint(-1, 1)

    player = Player("Koe", "@", 50, 10, 3)
    player.position = [20, 55]

    giant_ant = GiantAnt("Giant Ant", "A", 12, 5, 1)
    giant_ant.position = [random_inty, random_intx]
    epy, epx = giant_ant.position
    my, mx = int, int

    # clear → draw UI → draw entities → refresh

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
    stdscr.refresh()
    targetwin_h, targetwin_w = 10, 20
    playerwin_h, playerwin_w = 10, 20
    target_window = curses.newwin(targetwin_h, targetwin_w, 29, 99)
    player_window = curses.newwin(playerwin_h, playerwin_w, 29, 0)
    dbg = curses.newwin(12, 30, 1, 89)

    show_target = False
    prev_positions = []

    ant_dmg = player.st - giant_ant.df
    player_dmg = giant_ant.st - player.df

    while True:
        #stdscr.clear()
        for y, x in prev_positions:
            stdscr.addch(y, x, ord(" "))

        prev_positions = []

        target_window.box()
        player_window.box()
        dbg.box()
        # stdscr.addch(player.position[0], player.position[1], player.icon)
        # prev_positions.append(tuple(player.position))
        player.player_spawn(stdscr, prev_positions, player)
        giant_ant.monster_spawner(stdscr, prev_positions, e)
        # if giant_ant.alive:
        #     movement_area(stdscr, giant_ant.position[0], giant_ant.position[1])
        #     stdscr.addch(giant_ant.position[0], giant_ant.position[1], giant_ant.icon)
        #     prev_positions.append(tuple(giant_ant.position))


        stdscr.refresh()
        if show_target:
            target_window.addstr(1, 1, f"   {e.name}")
            target_window.addstr(3, 1, f" HP:   {e.hp}")
            target_window.addstr(5, 1, f"STR:   {e.st}")
            target_window.addstr(7, 1, f"DEF:   {e.df}")
            target_window.refresh()
        else:
            target_window.erase()
            target_window.box()
            target_window.refresh()

        player_window.addstr(1, 1, f"       {player.name}")
        player_window.addstr(3, 1, f" HP:   {player.hp}")
        player_window.addstr(5, 1, f"STR:   {player.st}")
        player_window.addstr(7, 1, f"DEF:   {player.df}")
        player_window.refresh()

        dbg.addstr(1, 1, f"Player: {player.position}")
        dbg.addstr(2, 1, f"eCords: {enemies[0].position}")
        dbg.addstr(3, 1, f"eCords: {e.position}")
        # dbg.addstr(4, 1, f"eCords: {enemies[2].position}")
        dbg.refresh()

        key = stdscr.getch()

        # px = 0
        # py = 0
        # ex = 0
        # ey = 0

        # if random_movement <= 4:
        #     ey = random_direction
        #     epy, epx = giant_ant.position
        # if 4 < random_movement <= 8:
        #     ex = random_direction
        #     epy, epx = giant_ant.position
        # if 8 < random_movement <= 10:
        #     ex = 0
        #     ey = 0

        #ney, nex = giant_ant.future_position(ey, ex)

        # if ney == player.position[0] and nex == player.position[1]:
        #     ex = 0
        #     ey = 0
        #     player.take_dmg(ant_dmg)
        #     player_window.erase()
        #     player_window.refresh()

        if key == ord("q"):
            break
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()
            show_target = mouse_actions(e, mx, my, player, bstate, show_target)
        # elif key == ord("a"):
        #     px = 1
        # elif key == ord("d"):
        #     px = -1
        # elif key == ord("w"):
        #     py = -1
        # elif key == ord("s"):
        #     py = 1
        # elif key == "":
        #     stdscr.refresh()
        #     continue
        # elif key == curses.KEY_MOUSE:
        #     _, mx, my, _, bstate = curses.getmouse()
        #     if bstate & curses.BUTTON1_PRESSED:
        #         if (my, mx) == (epy, epx):
        #             show_target = True
        #         elif (my, mx) != (epy, epx):
        #             show_target = False
        #     continue

        #ny, nx = player.future_position(py, px)

        # if ny == giant_ant.position[0] and nx == giant_ant.position[1]:
        #     px = 0
        #     py = 0
        #     giant_ant.take_dmg(player_dmg)
        #     target_window.erase()
        #     target_window.refresh()
        # elif ny == ney and nx == nex:
        #     px = 0
        #     py = 0

        # player.move(py, px)
        # giant_ant.move(ey, ex)
        # random_direction = random.randint(-1, 1)
        # random_movement = random.randint(1, 10)
        py, px = player.input_action(key)
        ey, ex = giant_ant.enemy_movement()

        world_event_logic(player, e, py, px, ey, ex, player_window, target_window, stdscr, random_inty,
                          random_intx)
        stdscr.refresh()

wrapper(gamestart)

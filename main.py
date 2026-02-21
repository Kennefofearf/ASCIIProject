import curses
import random
import time
from curses import wrapper
import player_module
from player_module import Player
import monster_module
from monster_module import GiantAnt

def mouse_actions(ant, mx, my, player, bstate, show_target):
    if bstate & curses.BUTTON1_PRESSED:
        if (my, mx) == tuple(ant.position):
            show_target = True
        else:
            show_target = False
    return show_target

def world_event_logic(player, ant, py, px, ey, ex, player_window, target_window, stdscr, random_inty, random_intx):
    ny, nx = player.future_position(py, px)
    ney, nex = ant.future_position(ey, ex)

    if ant.alive and (ney, nex) == tuple(player.position):
        ey = 0
        ex = 0
        player.take_dmg(max(0, ant.st - player.df))
        player_window.erase()
        player_window.refresh()

    if ant.alive and (ny, nx) == tuple(ant.position):
        py = 0
        px = 0
        ant.take_dmg(max(0, player.st - ant.df))
        target_window.erase()
        target_window.refresh()

    elif ant.alive and (ny, nx) == (ney, nex):
        py = 0
        px = 0

    player.move(py, px)
    if ant.alive:
        ant.move(ey, ex)
        stdscr.addch(ant.position[0], ant.position[1], ant.icon)


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

    field_enemies = [giant_ant, giant_ant, giant_ant]

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
        stdscr.addch(player.position[0], player.position[1], player.icon)
        prev_positions.append(tuple(player.position))
        # for enemy in field_enemies:
        #     enemy.position[0], enemy.position[1] = random.randint(1, 20), random.randint(1, 100)
        if giant_ant.alive:
            stdscr.addch(giant_ant.position[0], giant_ant.position[1], giant_ant.icon)
            prev_positions.append(tuple(giant_ant.position))


        stdscr.refresh()
        if show_target:
            target_window.addstr(1, 1, f"   {giant_ant.name}")
            target_window.addstr(3, 1, f" HP:   {giant_ant.hp}")
            target_window.addstr(5, 1, f"STR:   {giant_ant.st}")
            target_window.addstr(7, 1, f"DEF:   {giant_ant.df}")
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
        dbg.addstr(2, 1, f"EnemyArray : {field_enemies.count(giant_ant)}")
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
            show_target = mouse_actions(giant_ant, mx, my, player, bstate, show_target)
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

        world_event_logic(player, giant_ant, py, px, ey, ex, player_window, target_window, stdscr, random_inty,
                          random_intx)
        stdscr.refresh()

wrapper(gamestart)

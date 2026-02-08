import curses
import random
import time
from curses import wrapper
import player_module
from player_module import Player
import monster_module
from monster_module import GiantAnt

def gamestart(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    terminal_h, terminal_w = stdscr.getmaxyx()
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)

    stdscr.clear()

    random_inty, random_intx = random.randint(1, 20), random.randint(1, 100)
    random_timer = random.randint(3, 5)
    random_movement = random.randint(1, 10)
    random_direction = random.randint(-1, 1)

    player = Player("Koe", "@", 50, 10, 3)
    player.position = [20, 55]

    giant_ant = GiantAnt("Giant Ant", "A", 12, 5, 1)
    giant_ant.position = [random_inty, random_intx]
    epy, epx = giant_ant.position
    my, mx = int, int

    targetwin_h, targetwin_w = 10, 20
    playerwin_h, playerwin_w = 10, 20
    target_window = curses.newwin(targetwin_h, targetwin_w, 29, 99)
    player_window = curses.newwin(playerwin_h, playerwin_w, 29, 0)

    show_target = False

    while True:
        stdscr.clear()
        stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
        target_window.box()
        player_window.box()
        stdscr.addch(player.position[0], player.position[1], player.icon)
        stdscr.addch(giant_ant.position[0], giant_ant.position[1], giant_ant.icon)

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

        dbg = curses.newwin(12, 30, 0, 89)
        dbg.box()
        dbg.addstr(1, 1, f"Player: {player.position}")
        dbg.addstr(2, 1, f"Enemy : {giant_ant.position}")
        dbg.addstr(3, 1, f"tarw  : {targetwin_h, targetwin_w}")
        dbg.addstr(4, 1, f"epy   : {epy}")
        dbg.addstr(5, 1, f"epx   : {epx}")
        dbg.addstr(6, 1, f"mx    : {mx}")
        dbg.addstr(7, 1, f"my    : {my}")
        dbg.addstr(8, 1, f"Mouse: {curses.getmouse()}")
        dbg.addstr(9, 1, f"Button1: {curses.BUTTON1_PRESSED}")
        dbg.addstr(10, 1, f"Show_target: {show_target}")
        dbg.refresh()

        key = stdscr.getch()

        px = 0
        py = 0
        ex = 0
        ey = 0

        if random_movement <= 4:
            ey = random_direction
            epy, epx = giant_ant.position
        if 4 < random_movement <= 8:
            ex = random_direction
            epy, epx = giant_ant.position
        if 8 < random_movement <= 10:
            ex = 0
            ey = 0

        if key == ord("q"):
            break
        elif key == ord("a"):
            px = 1
        elif key == ord("d"):
            px = -1
        elif key == ord("w"):
            py = -1
        elif key == ord("s"):
            py = 1
        elif key == "":
            stdscr.refresh()
            continue
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_PRESSED:
                if (my, mx) == (epy, epx):
                    show_target = True
                elif (my, mx) != (epy, epx):
                    show_target = False
            continue

        ny, nx = player.future_position(py, px)
        ney, nex = giant_ant.future_position(ey, ex)

        if ny == giant_ant.position[0] and nx == giant_ant.position[1]:
            px = 0
            py = 0
        elif ney == player.position[0] and nex == player.position[1]:
            ex = 0
            ey = 0

        player.move(py, px)
        giant_ant.move(ey, ex)
        random_direction = random.randint(-1, 1)
        random_movement = random.randint(1, 10)
        stdscr.refresh()

wrapper(gamestart)

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

    stdscr.clear()

    random_inty, random_intx = random.randint(1, 20), random.randint(1, 100)
    random_timer = random.randint(3, 5)
    random_movement = random.randint(1, 10)
    random_direction = random.randint(-1, 1)

    player = Player("Koe", "@", 50, 10, 3)
    player.position = [20, 55]

    giant_ant = GiantAnt("Giant Ant", "A", 12, 5, 1)
    giant_ant.position = [random_inty, random_intx]

    targetwin_h, targetwin_w = terminal_h - 5, terminal_w - 100
    target_window = curses.newwin(targetwin_h, targetwin_w, 2, 2)

    while True:
        stdscr.clear()
        stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
        target_window.box()
        stdscr.addch(player.position[0], player.position[1], player.icon)
        stdscr.addch(giant_ant.position[0], giant_ant.position[1], giant_ant.icon)

        stdscr.refresh()
        target_window.refresh()
        key = stdscr.getch()

        px = 0
        py = 0
        ex = 0
        ey = 0

        if random_movement <= 4:
            ey = random_direction
        if 4 < random_movement <= 8:
            ex = random_direction
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

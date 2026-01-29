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

    while True:
        stdscr.clear()
        stdscr.border("#", "#", "#", "#", "O", "O", "O", "O")
        stdscr.addch(player.position[0], player.position[1], player.icon)
        stdscr.addch(giant_ant.position[0], giant_ant.position[1], giant_ant.icon)
        stdscr.refresh()

        # Monster movement
        anty, antx = 0, 0

        # if random_movement <= 5:
        #     anty = random_direction
        #     giant_ant.move(anty, antx)
        #     anty = 0
        # elif random_movement > 5:
        #     antx = random_direction
        #     giant_ant.move(anty, antx)
        #     antx = 0

        stdscr.refresh()
        key = stdscr.getch()

        px = 0
        py = px

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

        if ny == giant_ant.position[0] and nx == giant_ant.position[1]:
            break

        player.move(py, px)
        random_movement = random.randint(1, 10)
        stdscr.refresh()

wrapper(gamestart)

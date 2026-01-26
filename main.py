import curses
import random
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
    random_timer = random.randint(3, 15)
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

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == ord("a"):
            player.move(0, 1)
        elif key == ord("d"):
            player.move(0, -1)
        elif key == ord("w"):
            player.move(-1, 0)
        elif key == ord("s"):
            player.move(1, 0)

    # while True:
    #     # Monster movement
    #     anty, antx = 0, 0
    #     if random_movement <= 5:
    #         anty = random_direction
    #         giant_ant.move(anty, antx, random_timer)
    #     elif random_movement > 5:
    #         antx = random_direction
    #         giant_ant.move(anty, antx, random_timer)


wrapper(gamestart)

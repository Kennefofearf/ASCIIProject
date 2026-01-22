import curses
import time
from curses import wrapper


def gamestart(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.clear()

    playery, playerx = 10, 10

    while True:
        stdscr.clear()
        player = stdscr.addch(playery, playerx, "@")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == ord("a"):
            playerx -= 1
        elif key == ord("d"):
            playerx += 1
        elif key == ord("w"):
            playery -= 1
        elif key == ord("s"):
            playery += 1

wrapper(gamestart)

import curses
from curses import wrapper


def gamestart(stdscr):
    curses.cbreak()
    curses.noecho()
    stdscr.clear()

    stdscr.addch(10, 40, "@")
    stdscr.getch()


wrapper(gamestart)

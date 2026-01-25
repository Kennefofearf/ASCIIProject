import curses
from curses import wrapper
import player_module
from player_module import Player


def gamestart(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)

    stdscr.clear()

    player = Player("Koe", "@", 50, 10, 3)
    player.position = [20, 55]

    while True:
        stdscr.clear()
        stdscr.border("#", "#", "#", "#", "O", "O", "O", "O")
        stdscr.addch(player.position[0], player.position[1], player.icon)
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

wrapper(gamestart)

import curses


def title_screen(stdscr):
    screen_y, screen_x = stdscr.getmaxyx()

    start_y, start_x = screen_y // 2, screen_x // 2

    title = f"Python Role-Playing Game"

    title_scr = curses.newwin(screen_y, screen_x)

    new_game_option = f"[A] NEW GAME"
    quit_option = f"[Q] QUIT"
    continue_option = f"[W] CONTINUE"

    title_scr.addstr(start_y, start_x - (len(title) // 2), title)

    row = start_y + 10

    title_scr.addstr(row, start_x - (len(new_game_option) // 2), new_game_option)
    row += 5
    title_scr.addstr(row, start_x - (len(quit_option) // 2), quit_option)

    title_scr.refresh()

    while True:
        key = title_scr.getch()

        if key == ord("a"):
            return "new_game"

        elif key == ord("q"):
            return "quit"

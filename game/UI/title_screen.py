import curses


def title_screen(stdscr, saved_characters):
    screen_y, screen_x = stdscr.getmaxyx()

    start_y, start_x = screen_y // 2, screen_x // 2

    title = f"Python Role-Playing Game"

    title_scr = curses.newwin(screen_y, screen_x)

    new_game_option = f"[A] NEW GAME"
    quit_option = f"[Q] QUIT"
    continue_option = f"[W] CONTINUE"

    title_scr.addstr(start_y, start_x - (len(title) // 2), title)

    row = start_y + 10

    can_continue = bool(saved_characters)

    title_scr.addstr(row, start_x - (len(new_game_option) // 2), new_game_option)
    row += 2

    if saved_characters:
        title_scr.addstr(row, start_x - (len(continue_option) // 2), continue_option)
        can_continue = True
        row += 2
    else:
        can_continue = False

    title_scr.addstr(row, start_x - (len(quit_option) // 2), quit_option)

    title_scr.refresh()

    while True:
        key = title_scr.getch()

        if key == ord("a"):
            return "new_game"

        elif key == ord("w"):
            if can_continue:
                return "continue"
            else:
                continue

        elif key == ord("q"):
            return "quit"

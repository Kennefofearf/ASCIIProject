import curses


def character_select_screen(stdscr, saved_characters):
    screen_y, screen_x = stdscr.getmaxyx()

    selected_index = 0

    char_select_window = curses.newwin(screen_y, screen_x)

    while True:
        char_select_window.clear()
        char_select_window.box()

        row = 1

        for index, character_name in enumerate(saved_characters):
            if index == selected_index:
                char_select_window.addstr(row, 1, character_name, curses.A_REVERSE)
            else:
                char_select_window.addstr(row, 1, character_name)

        row += 1

        char_select_window.refresh()

        key = char_select_window.getch()

        if key == ord("w"):
            if selected_index == 0:
                selected_index = len(saved_characters) - 1
            else:
                selected_index -= 1
        elif key == ord("s"):
            if selected_index == len(saved_characters) - 1:
                selected_index = 0
            else:
                selected_index += 1
        elif key in (10, 13):
            return saved_characters[selected_index]

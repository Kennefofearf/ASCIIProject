import curses

def character_creation_screen(stdscr):
    screen_y, screen_x = stdscr.getmaxyx()

    start_y, start_x = screen_y // 2, screen_x // 2

    name_prompt = f"What should we call you?"
    name = ""
    max_name_length = 8

    creation_scr = curses.newwin(screen_y, screen_x)

    while True:
        creation_scr.clear()

        creation_scr.addstr(start_y, start_x - (len(name_prompt) // 2), name_prompt)
        creation_scr.addstr(start_y + 5, start_x - (len(name_prompt) // 2), name)

        creation_scr.refresh()

        key = creation_scr.getch()

        if key in (curses.KEY_BACKSPACE, 127, 8):
            name = name[:-1]

        elif key in (10, 13):
            if name:
                if name != "":
                    return name

        elif 32 <= key <= 126:
            if len(name) < max_name_length:
                name += chr(key)


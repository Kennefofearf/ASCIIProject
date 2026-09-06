import curses


def create_combat_log_windows(stdscr):
    logwin_h, logwin_w, y, x = 10, 77, 29, 21
    outer_log_window = curses.newwin(logwin_h, logwin_w, y, x)
    outer_log_window.refresh()

    inner_log_window = curses.newwin(logwin_h - 2, logwin_w - 2, y + 1, x + 1)
    inner_log_window.scrollok(True)
    inner_log_window.idlok(True)
    inner_log_window.refresh()

    return outer_log_window, inner_log_window, logwin_h, logwin_w


def draw_log(log_win, combat_messages, scroll_offset):
    h, w = log_win.getmaxyx()
    log_win.erase()

    start = max(0, len(combat_messages) - h - scroll_offset)
    visible = combat_messages[start:start + h]

    for row, message_pair in enumerate(visible):
        col = 0
        for text, color_pair in message_pair:
            text = str(text)

            if color_pair == 0:
                log_win.addstr(row, col, text[:w-col])
            else:
                log_win.addstr(row, col, text[:w-col], curses.color_pair(color_pair))

            col += len(text)

    log_win.refresh()
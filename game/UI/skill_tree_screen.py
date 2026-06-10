import curses

def draw_node(window, y, x, label=""):
    window.addstr(y, x, "_____")
    window.addstr(y + 1, x, "|     |")
    window.addstr(y+ 2, x, f"|{label:^5}|")
    window.addstr(y + 3, x, "|_____|")

def open_skill_tree(stdscr, selected_item):

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        skill_tree_window = curses.newwin(height, tree_width, start_y, tree_x)

        skill_tree_window.box()

        key = stdscr.getch()

        if key == ord("k"):
            skill_tree_window.erase()
            skill_tree_window.refresh()
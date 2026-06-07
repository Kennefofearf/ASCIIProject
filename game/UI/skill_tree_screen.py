import curses

def open_skill_tree(stdscr, selected_item):

    while True:
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        height = int(stdscr_y * 0.7)
        tree_width = int(stdscr_x * 0.35)
        start_y = int(stdscr_y * 0.15)
        tree_x = int(stdscr_x * 0.55)

        skill_tree_window = curses.newwin(height, tree_width, start_y, tree_x)

        skill_tree_window.box()

        skill_tree_dividers = "_" * (tree_width - 2)

        skill_tree_window.addstr(1, int(tree_width / 2), f"|")
        skill_tree_window.addstr(2, int(tree_width / 2), f"|")
        skill_tree_window.addstr(3, int(tree_width / 2), f"|")
        skill_tree_window.addstr(4, int(tree_width / 2), f"|")
        skill_tree_window.addstr(4, 1, f"{skill_tree_dividers}")

        skill_tree_window.refresh()

        key = stdscr.getch()

        if key == ord("k"):
            skill_tree_window.erase()
            skill_tree_window.refresh()
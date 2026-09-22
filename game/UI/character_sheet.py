import curses


def show_character_sheet(stdscr, player):
    screen_y, screen_x = stdscr.getmaxyx()

    while True:
        sheet_height = int(screen_y * 0.7)
        sheet_width = int(screen_x * 0.55)
        start_y = int(screen_y * 0.15)
        start_x = int(screen_x * 0.10)

        character_sheet_window = curses.newwin(sheet_height, sheet_width, start_y, start_x)

        sheet_x, sheet_y = character_sheet_window.getmaxyx()

        character_sheet_window.erase()
        character_sheet_window.box()

        character_sheet_window.addstr(1, sheet_x - (len(player.name) // 2), f"{player.name}")
        character_sheet_window.addstr(3, 1, f" HP: {player.hp} / {player.max_hp}")
        character_sheet_window.addstr(4, 1, f"STR: {player.st}")
        character_sheet_window.addstr(5, 1, f"DEF: {player.df}")
        character_sheet_window.addstr(6, 1, f" AC: {player.ac}")
        character_sheet_window.addstr(7, 1, f"MGP: {player.mp}")
        character_sheet_window.addstr(8, 1, f"EVA: {player.evasion}")
        character_sheet_window.addstr(9, 1, f"CRT: {player.crit_rate}")
        character_sheet_window.addstr(10, 1, f"CRD: {player.crit_dmg}")
        character_sheet_window.addstr(11, 1, f"HRR: {player.hp_rr}")
        character_sheet_window.addstr(12, 1, f"HRA: {player.hp_ra}")

        character_sheet_window.addstr(14, sheet_x - (len("EQUIPMENT") // 2), f"EQUIPMENT")
        character_sheet_window.addstr(16, 1,
                                      f" Head: {player.head.name} | Lvl: {player.head.lvl} / {player.head.max_lvl}")
        character_sheet_window.addstr(17, 1,
                                      f"Chest: {player.chest.name} | Lvl: {player.chest.lvl} / {player.chest.max_lvl}")
        character_sheet_window.addstr(18, 1,
                                      f" Feet: {player.feet.name} | Lvl: {player.feet.lvl} / {player.feet.max_lvl}")
        character_sheet_window.addstr(
            19, 1, f"  Wpn: {player.weapon.name} | Lvl: {player.weapon.lvl} / {player.weapon.max_lvl}"
        )

        character_sheet_window.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            if character_sheet_window:
                character_sheet_window.clear()
                character_sheet_window.refresh()
                break

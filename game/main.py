import curses
from curses import wrapper
from systems.combat import player_auto_attack_logic, enemy_auto_attack_logic
from player_module import Player
from monster_module import GiantAnt

enemies = []

for enemy in range(3):
    e = GiantAnt()
    enemies.append(e)

def mouse_actions(mx, my, bstate, player):
    if bstate & curses.BUTTON1_CLICKED:
        for enemy in enemies:
            if (my, mx) == tuple(enemy.position) and enemy.alive:
                player.target = enemy
                return True, enemy
        return True, None
    return False, None

def draw_enemies(stdscr, enemies, selected, prev_positions):
    for enemy in enemies:
        if not enemy.alive:
            continue

        y, x = enemy.position

        if enemy == selected:
            attr = curses.color_pair(1)
        else:
            attr = curses.A_NORMAL

        stdscr.addch(y, x, enemy.icon, attr)
        prev_positions.append((y, x))


def world_event_logic(player, py, px, stdscr, combat_messages, inner, scroll_offset):
    ny, nx = player.future_position(py, px)
    if not movement_area(stdscr, ny, nx):
        py = 0
        px = 0

    player_hit = player_auto_attack_logic(player, add_log_messages, combat_messages)
    enemy_hit = enemy_auto_attack_logic(enemies, player, add_log_messages, combat_messages)

    if player_hit or enemy_hit:
        draw_log(inner, combat_messages, scroll_offset)

    for e in enemies:
        e.respawn_timer(player)
        if e.alive == False:
            continue

        ey, ex = e.enemy_random_movement()
        ney, nex = e.future_position(ey, ex)

        if not movement_area(stdscr, ney, nex):
            ey = 0
            ex = 0

        elif (ney, nex) == tuple(player.position):
            ey = 0
            ex = 0

        elif (ny, nx) == tuple(e.position):
            py = 0
            px = 0

        elif (ny, nx) == (ney, nex):
            py = 0
            px = 0

        e.move(ey, ex)

    player.move(py, px)

def movement_area(win, y, x):
    h, w = win.getmaxyx()
    return 1 <= y <= h - 2 and 1 <= x <= w - 2

def create_combat_log_windows(stdscr):
    logwin_h, logwin_w, y, x = 10, 77, 29, 21
    outer_log_window = curses.newwin(logwin_h, logwin_w, y, x)
    outer_log_window.refresh()

    inner_log_window = curses.newwin(logwin_h - 2, logwin_w - 2, y + 1, x + 1)
    inner_log_window.scrollok(True)
    inner_log_window.idlok(True)
    inner_log_window.refresh()

    return outer_log_window, inner_log_window, logwin_h, logwin_w

def add_log_messages(combat_messages, message_pair):
    if len(combat_messages) > 200:
        combat_messages.pop(0)

    combat_messages.append(message_pair)

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

def gamestart(stdscr):
    curses.cbreak()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(200)
    stdscr.timeout(17)
    selected = None

    stdscr.clear()

    y, x = stdscr.getmaxyx()
    player = Player("Koe", "@", 50, 50, 21, 3, 4, 1)
    player.position = [20, 55]

    # Window rendering

    stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
    stdscr.refresh()
    targetwin_h, targetwin_w = 10, 20
    playerwin_h, playerwin_w = 10, 20
    target_window = curses.newwin(targetwin_h, targetwin_w, int(y * 0.73), int(x * 0.83))
    player_window = curses.newwin(playerwin_h, playerwin_w, int(y * 0.73), int(x * 0.01))
    dbg_h, dbg_w = 15, 30
    dbg = curses.newwin(dbg_h, dbg_w, y - (y - 1), x - (x - 89))

    prev_positions = []

    outer, inner, outer_h, outer_w = create_combat_log_windows(stdscr)
    combat_messages = []
    log_height = inner.getmaxyx()[0]
    scroll_offset = 0

    while True:
        #time.sleep(0.5)
        #time.sleep(2)
        for y, x in prev_positions:
            stdscr.addch(y, x, ord(" "))

        prev_positions = []

        target_window.box()
        player_window.box()
        dbg.box()

        player.player_spawn(stdscr, prev_positions, player)
        draw_enemies(stdscr, enemies, selected, prev_positions)

        stdscr.refresh()

        if selected and selected.alive:
            target_window.addstr(1, 1, f"   {selected.name}")
            target_window.addstr(3, 1, f" HP:   {selected.hp} / {selected.max_hp}")
            target_window.addstr(5, 1, f"STR:   {selected.st}")
            target_window.addstr(7, 1, f"DEF:   {selected.df}")
            dbg.addstr(1, 1, f"{selected.name}")
            target_window.refresh()
        else:
            target_window.erase()
            target_window.box()
            target_window.refresh()

        player_window.addstr(1, 1, f"       {player.name}")
        player_window.addstr(2, 1, f"Lvl:   {player.lvl}")
        player_window.addstr(3, 1, f" HP:   {player._hp} / {player.max_hp}")
        player_window.addstr(4, 1, f"STR:   {player._st}")
        player_window.addstr(5, 1, f"DEF:   {player._df}")
        player_window.addstr(6, 1, f"Nxt:   {player.req_xp}")
        player_window.refresh()

        dbg.addstr(1, 1, f"Inventory: {player.inventory}")
        dbg.refresh()

        key = stdscr.getch()
        my = 0
        mx = 0

        if key == ord("q"):
            break
        elif key == curses.KEY_RESIZE:
            stdscr.clear()
            stdscr_y, stdscr_x = stdscr.getmaxyx()
            resize_x = stdscr_x
            target_window = curses.newwin(targetwin_h, targetwin_w, int((stdscr_y - 10) * 0.99), int((stdscr_x - 20) *
                                                                                                     0.99))
            dbg = curses.newwin(dbg_h, dbg_w, int(stdscr_y * 0.03), int(stdscr_x * 0.99) - 30)
            player_window = curses.newwin(playerwin_h, playerwin_w, int((stdscr_y - 10) * 0.99), int(stdscr_x * 0.01))

            outer = curses.newwin(outer_h, outer_w, int((stdscr_y - 10) * 0.99), int((stdscr_x * 0.01) + 21))
            inner = curses.newwin(outer_h - 2, outer_w - 2, int((stdscr_y - 9) * 0.99), int((stdscr_x * 0.01) + 23))
            outer.box()
            outer.refresh()
            inner.box()
            inner.refresh()
            stdscr.border(ord("#"), ord("#"), ord("#"), ord("#"), ord("O"), ord("O"), ord("O"), ord("O"))
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, bstate, = curses.getmouse()

            clicked, picked = mouse_actions(mx, my, bstate, player)
            selected = picked
            player.target = picked

        scroll_log_y, scroll_log_x = inner.getbegyx()
        scroll_log_h, scroll_log_w = inner.getmaxyx()

        if scroll_log_y <= my < scroll_log_y + scroll_log_h and scroll_log_x <= mx < scroll_log_x + scroll_log_w:

            if bstate & curses.BUTTON4_PRESSED:
                scroll_offset += 1
            elif bstate & curses.BUTTON5_PRESSED:
                scroll_offset = max(0, scroll_offset - 1)

            max_scroll = max(0, len(combat_messages) - log_height)
            scroll_offset = min(scroll_offset, max_scroll)

        draw_log(inner, combat_messages, scroll_offset)

        py, px = player.input_action(key)

        world_event_logic(player, py, px, stdscr, combat_messages, inner, scroll_offset)

        if selected and not selected.alive:
            selected = None

        stdscr.refresh()

wrapper(gamestart)

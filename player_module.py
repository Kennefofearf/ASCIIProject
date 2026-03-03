import curses
import monster_module


class Player:
    def __init__(self, name, icon, hp, st, df, req_xp, lvl):
        self.name = name
        self.icon = "@"
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [0, 0]
        self.req_xp = req_xp
        self.lvl = lvl

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px

    def future_position(self, py, px):
        return (self.position[0] + py, self.position[1] - px)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0

    def xp_gain(self, xp):
        last_req_xp = self.req_xp
        self.req_xp -= xp
        if self.req_xp <= 0:
            self.req_xp = last_req_xp * 2
            self.lvl += 1


    def input_action(self, key):
        py, px = 0, 0
        if key == ord("a"):
            px = 1
        elif key == ord("d"):
            px = -1
        elif key == ord("w"):
            py = -1
        elif key == ord("s"):
            py = 1
        elif key == "":
            py, px = 0, 0
        return py, px

    def player_spawn(self, stdscr, prev_positions, player):
        stdscr.addch(player.position[0], player.position[1], player.icon)
        prev_positions.append(tuple(player.position))

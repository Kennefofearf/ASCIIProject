import curses
import monster_module
import random


class Player:
    def __init__(self, name, icon, max_hp, hp, st, df, req_xp, lvl):
        self.name = name
        self.icon = "@"
        self.max_hp = max_hp
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
        self.req_xp -= xp
        if self.req_xp <= 0:
            xp_overflow = -self.req_xp
            self.lvl += 1
            hp_gain = random.choice([5, 7, 7, 7, 10, 20])
            self.max_hp += hp_gain
            self.hp += hp_gain
            self.st += random.choice([1, 1, 0, 2])
            self.df += random.choice([1, 1, 1, 0])
            self.req_xp += 4 + self.lvl * 5
            self.req_xp -= xp_overflow


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

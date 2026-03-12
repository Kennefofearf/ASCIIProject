import curses
import monster_module
import random
import time



class Player:
    def __init__(self, name, icon, max_hp, hp, st, df, req_xp, lvl):
        self.name = name
        self.icon = "@"
        self.max_hp = max_hp
        self._hp = hp
        self._st = st
        self._df = df
        self.position = [0, 0]
        self.req_xp = req_xp
        self.lvl = lvl
        self.weapon = None
        self.target = None
        self.attack_cooldown = 1.0
        self.last_attack_time = 0

    @property
    def hp(self):
        return self.max_hp + (self.weapon.total_bonus("max_hp") if self.weapon else 0)

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    @property
    def st(self):
        return self.st + (self.weapon.total_bonus("st") if self.weapon else 0)

    @st.setter
    def st(self, value):
        self._st = max(0, value)

    @property
    def df(self):
        return self.df + (self.weapon.total_bonus("df") if self.weapon else 0)

    @df.setter
    def st(self, value):
        self._df = max(0, value)

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px

    def future_position(self, py, px):
        return (self.position[0] + py, self.position[1] - px)

    def take_dmg(self, dmg):
        self._hp -= dmg
        if self._hp <= 0:
            self._hp = 0

    def xp_gain(self, xp):
        self.req_xp -= xp
        if self.req_xp <= 0:
            xp_overflow = -self.req_xp
            self.lvl += 1
            hp_gain = random.choice([5, 7, 7, 7, 10, 20])
            self.max_hp += hp_gain
            self._hp += hp_gain
            self._st += random.choice([1, 1, 0, 2])
            self._df += random.choice([1, 1, 1, 0])
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

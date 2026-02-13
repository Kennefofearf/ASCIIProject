import curses
import monster_module


class Player:
    def __init__(self, name, icon, hp, st, df):
        self.name = name
        self.icon = "@"
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [0, 0]

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px

    def future_position(self, py, px):
        return (self.position[0] + py, self.position[1] - px)

    def take_dmg(self, dmg):
        self.hp -= dmg

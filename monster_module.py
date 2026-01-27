import curses
import time

class GiantAnt:
    def __init__(self, name, icon, hp, st, df):
        self.name = "Giant Ant"
        self.icon = "A"
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [0, 0]

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px



import curses

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


import curses
import time
import random

class GiantAnt:

    def __init__(self, name, icon, hp, st, df):
        self.name = "Giant Ant"
        self.icon = "A"
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [0, 0]

        self.random_movement = random.randint(1, 10)
        self.random_direction = random.randint(-1, 1)

        self.idle = 0.0

    def enemy_movement(self):
        now = time.monotonic()
        if now < self.idle:
            return 0, 0

        ey, ex = 0, 0

        rmove = self.random_movement
        rdirect = self.random_direction

        if rmove <= 4:
            ey = rdirect
        elif rmove <= 8:
            ex = rdirect
        else:
            ey = 0
            ex = 0

        self.random_movement = random.randint(1, 10)
        self.random_direction = random.randint(-1, 1)

        if random.randint(1, 3) == 1:
            self.idle = now + random.uniform(2, 4)

        return ey, ex

    def move(self, ey, ex):
        self.position[0] += ey
        self.position[1] -= ex

    def future_position(self, ey, ex):
        return (self.position[0] + ey, self.position[1] - ex)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0

    def input_action(self, key):
        py, px = 0, 0


import curses
import time
import random

class Monster:

    def __init__(self, name, icon, hp, st, df):
        self.name = name
        self.icon = icon
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [0, 0]
        self.alive = True

        self.random_movement = random.randint(1, 10)
        self.random_direction = random.randint(-1, 1)

        self.idle = 0.0

    def enemy_movement(self):
        now = time.monotonic()
        if now < self.idle:
            return 0, 0

        ey, ex = 0, 0

        ey = random.choice([-1, 0, 1])
        ex = random.choice([-1, 0, 1])

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
            self.alive = False

    def monster_spawner(self, stdscr, prev_positions, enemy):
        if enemy.alive:
            # movement_area(stdscr, enemy.position[0], enemy.position[1])
            stdscr.addch(enemy.position[0], enemy.position[1], enemy.icon)
            prev_positions.append(tuple(enemy.position))

class GiantAnt(Monster):
    def __init__(self, name="Giant Ant", icon="A", hp=12, st=5, df=1):
        super().__init__(name, icon, hp, st, df)

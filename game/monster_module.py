import curses
import time
import random
import pdb

class Monster:

    def __init__(self, name, icon, max_hp, hp, st, df, xp, respawn_delay, attack_cooldown):
        self.name = name
        self.icon = icon
        self.max_hp = max_hp
        self.hp = hp
        self.st = st
        self.df = df
        self.position = [random.randint(2, 19), random.randint(2, 99)]
        self.alive = True
        self.xp = xp
        self.respawn_delay = respawn_delay
        self.attack_cooldown = attack_cooldown
        self.last_attack_time = 0
        self.is_attacking = False
        self.damaged = False
        self.ey = 0
        self.ex = 0
        self.random_movement = random.randint(1, 10)
        self.random_direction = random.randint(-1, 1)

        self.idle = 0.0

    def enemy_random_movement(self):
        ey, ex = 0, 0
        if not self.is_attacking:
            ey = 0
            ex = 0
            now = time.monotonic()
            if now < self.idle:
                return 0, 0

            ey = random.choice([-1, 0, 1])
            ex = random.choice([-1, 0, 1])

            if random.randint(1, 3) == 1:
                self.idle = now + random.uniform(2, 4)

            return ey, ex
        return ey, ex

    def move(self, ey, ex):
        if not self.is_attacking:
            if self.alive:
                self.position[0] += ey
                self.position[1] -= ex
        return

    def future_position(self, ey, ex):
        return (self.position[0] + ey, self.position[1] - ex)

    def take_dmg(self, dmg):
        self.hp -= dmg
        self.damaged = True
        if self.hp <= 0:
            self.hp = 0
            self.respawn_delay = time.monotonic() + 3
            self.alive = False

    def respawn_timer(self, player):
        if not self.alive and self.respawn_delay is not None and time.monotonic() >= self.respawn_delay:
            self.alive = True
            self.hp = self.max_hp
            self.respawn_delay = None
            if self.position == player.position:
                self.position = [random.randint(2, 19), random.randint(2, 99)]


class GiantAnt(Monster):
    def __init__(self, name="Giant Ant", icon="A", max_hp=20, hp=20, st=5, df=1, xp=2):
        super().__init__(name, icon, max_hp, hp, st, df, xp, respawn_delay=None, attack_cooldown=2.0)

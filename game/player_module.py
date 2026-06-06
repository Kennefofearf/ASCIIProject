import curses
import monster_module
import random
from data.skill_node_data import COMMON_NODES
from data.affix_data import UNCOMMON_AFFIXES
import time



class Player:
    def __init__(self, name, icon, max_hp, hp, st, df, req_xp, total_req_xp, xp_bar_text, lvl):
        self.name = name
        self.icon = "@"
        self._max_hp = max_hp
        self._hp = hp
        self._st = st
        self._df = df
        self.base_max_hp = 50
        self.base_st = 21
        self.base_df = 3
        self.weapon_dmg = [0, 0]
        self.position = [0, 0]
        self.req_xp = req_xp
        self.total_req_xp = total_req_xp
        self.xp_bar_text = xp_bar_text
        self.lvl = lvl
        self.weapon = None
        # self.armor = None
        # self.boots = None
        # self.helm = None
        self.target = None
        self.skill_tree = {}
        self.abilities = []
        self.damaged = False
        self.active_effects = []
        self.attack_cooldown = 1.0
        self.last_attack_time = 0
        self.inventory = []

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    @property
    def max_hp(self):
        bonus = 0

        if self.weapon:
            bonus += self.weapon.get("base_stats", {}).get("max_hp", 0)

            for affix_id in self.weapon.get("affixes", []):
                affix_data = UNCOMMON_AFFIXES.get(affix_id, {})
                bonus += affix_data.get("affix_stats", {}).get("max_hp", 0)

        return self._max_hp + bonus

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = max(1, value)

        if self._hp > self.max_hp:
            self._hp = self.max_hp

    @property
    def st(self):
        bonus = 0

        if self.weapon:
            bonus += self.weapon.get("base_stats", {}).get("st", 0)

            for affix_id in self.weapon.get("affixes", []):
                affix_data = UNCOMMON_AFFIXES.get(affix_id, {})
                bonus += affix_data.get("affix_stats", {}).get("st", 0)

        if self.skill_tree is not None:
            for skill_id, skill_state in self.skill_tree.items():
                points = skill_state.get("points", 0)

                if points <= 0:
                    continue

                skill_data = COMMON_NODES.get(skill_id, {})
                bonus += skill_data.get("stats", {}).get("st", 0) * points

        for effect in self.active_effects:
            if effect["effect_id"] == "st_up":
                bonus += effect["value"]

        return self._st + bonus

    @st.setter
    def st(self, value):
        self._st = max(0, value)

    @property
    def df(self):
        bonus = 0

        if self.weapon:
            bonus += self.weapon.get("base_stats", {}).get("df", 0)

            for affix_id in self.weapon.get("affixes", []):
                affix_data = UNCOMMON_AFFIXES.get(affix_id, {})
                bonus += affix_data.get("affix_stats", {}).get("df", 0)

        if self.skill_tree is not None:
            for skill_id, skill_state in self.skill_tree.items():
                points = skill_state.get("points", 0)

                if points <= 0:
                    continue

                skill_data = COMMON_NODES.get(skill_id, {})
                bonus += skill_data.get("stats", {}).get("df", 0) * points

        for effect in self.active_effects:
            if effect["effect_id"] == "df_up":
                bonus += effect["value"]

        return self._df + bonus

    @df.setter
    def df(self, value):
        self._df = max(0, value)

    def move(self, py, px):
        self.position[0] += py
        self.position[1] -= px

    def future_position(self, py, px):
        return (self.position[0] + py, self.position[1] - px)

    def take_dmg(self, dmg):
        if dmg <= 0:
            dmg = 0
        self._hp -= dmg
        self.damaged = True
        if self._hp <= 0:
            self._hp = 0

    # Updates the XP bar

    def update_xp_bar(self):
        progress = self.total_req_xp - self.req_xp
        bar_count = int((progress / self.total_req_xp) * 10)

        self.xp_bar_text = '=' * bar_count

    # Calculates XP gain and uses it to update the XP bar

    def xp_gain(self, xp):
        self.req_xp -= xp

        while self.req_xp <= 0:
            xp_overflow = -self.req_xp
            self.lvl += 1
            hp_gain = random.choice([5, 7, 7, 7, 10, 20])
            self.max_hp += hp_gain
            self._hp += hp_gain
            self.total_req_xp += 5 + self.lvl * 5
            self.req_xp = self.total_req_xp - xp_overflow
            #self.req_xp -= xp_overflow

        self.update_xp_bar()

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

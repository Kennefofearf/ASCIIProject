import curses
import random
from systems.loot_generator import roll_item_drop
from UI.colors import get_rarity_color
from data.weapons import Weapons
import time

def is_adjacent(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y1 - y2) + abs(x1 - x2) == 1


def player_auto_attack_logic(player, add_log_messages, combat_messages):
    target = player.target

    if target is None:
        return

    if not target.alive:
        player.target = None
        return

    if is_adjacent(player.position, target.position):
        now = time.time()
        if now - player.last_attack_time >= player.attack_cooldown:

            if player.weapon:
                dmg = (random.randint((player.weapon.get('min_dmg') + player.st),
                       (player.weapon.get('max_dmg') + player.st))) - target.df
            else:
                dmg = player.st - target.df

            if dmg <= 0:
                dmg = 0

            target.take_dmg(max(0, dmg))
            player.last_attack_time = now

            if player.weapon:
                amount = 1
                Weapons.gain_item_xp(player.weapon, player.weapon, amount)

            add_log_messages(combat_messages, [(f"{target.name} ", 1), ("is hit for ", 0), (f"{dmg}", 2),
                                               ("!", 0)])

        if not target.alive:
            player.xp_gain(target.xp)

            dropped_item = roll_item_drop(target)

            if dropped_item:
                player.inventory.append(dropped_item)

                item_color = get_rarity_color(dropped_item)

                add_log_messages(combat_messages, [(f"Picked up: ", 0),
                                                   (f"{dropped_item['name']}", item_color)])

            player.target = None


def enemy_auto_attack_logic(enemies, player, add_log_messages, combat_messages):

    for enemy in enemies:
        if not enemy.alive:
            continue

        if is_adjacent(enemy.position, player.position):
            enemy.is_attacking = True
            now = time.time()
            if now - enemy.last_attack_time >= enemy.attack_cooldown:
                dmg = enemy.st - player.df

                if dmg <= 0:
                    dmg = 0

                player.take_dmg(max(0, dmg))
                enemy.last_attack_time = now
                add_log_messages(combat_messages,
                                 [(f"{player.name} ", 2), ("is hit for ", 0), (f"{dmg}", 1), ("!", 0)])
                # draw_log(inner, combat_messages, scroll_offset)
                # player_window.erase()
                # player_window.refresh()
        else:
            enemy.is_attacking = False

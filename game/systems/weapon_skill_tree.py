from game.data.weapon_skills_data import COMMON_SKILLS
from game.systems.ability_logic import rebuild_abilities

def can_activate(player, skill_id):
    skill = COMMON_SKILLS["skill_id"]

    for req in skill.get("requires", []):
        if player.skill_tree[req]["points"] <= 0:
            return False

    return True

def assign_points(player, skill_id):
    skill_data = COMMON_SKILLS["skill_id"]
    skill_state = player.skill_tree["skill_id"]

    if skill_state["points"] >= skill_data["max_points"]:
        return False, "Maxed"

    if not can_activate(player, skill_id):
        return False, "Prerequisites not met."

    skill_state["points"] += 1

    for ability in skill_data.get("unlocks", []):
        player.abilities.add(ability)

    return True

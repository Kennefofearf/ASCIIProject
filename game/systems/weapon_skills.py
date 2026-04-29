from game.data.weapon_skills_data import COMMON_SKILLS
from game.systems.ability_logic import rebuild_abilities

def is_active(skill_id, ability_id):
    current_points = COMMON_SKILLS[skill_id]["points"]
    max_points = COMMON_SKILLS[skill_id]["max_points"]
    if (current_points > 0):
        COMMON_SKILLS[skill_id]["unlocks"][ability_id]

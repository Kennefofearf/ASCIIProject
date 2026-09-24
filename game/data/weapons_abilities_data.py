from modules.ability_module import Ability
from modules.effect_module import DamageEffect, DotEffect


COMMON_WEAPON_ABILITIES = {
    "gash": Ability(
        ability_id="gash",
        name="Gash",
        tooltip="Give the target a deep cut that bleeds 2 damage/1 secs for 5 seconds.",
        cooldown=16,
        range=1,
        target_type="enemy",
        effects=[
            DamageEffect(
                base_dmg=3,
                scaling_stat="st",
                scaling=0.1,
                dmg_type=["physical", "slash"]
            ),
            DotEffect(
                effect_id="bleed",
                name="bleed_gash",
                verb=f"bleeds for",
                damage=2,
                interval=1.0,
                duration=5.0
            )
        ]
    ),
    "bash": Ability(
        ability_id="bash",
        name="Bash",
        tooltip="Hit the target with the hilt of your weapon for 10 damage.",
        cooldown=10,
        range=1,
        target_type="enemy",
        effects=[
            DamageEffect(
                base_dmg=10,
                scaling_stat="st",
                scaling=0.1,
                dmg_type=["physical", "blunt"]
            )
        ]
    ),
    "quick hit": Ability(
        ability_id="quick hit",
        name="Quick Hit",
        tooltip="Hit the target quickly for 5 damage. Fast cooldown.",
        cooldown=3,
        range=1,
        target_type="enemy",
        effects=[
            DamageEffect(
                base_dmg=5,
                scaling_stat="evasion",
                scaling=0.2,
                dmg_type=["physical"]
            )
        ]
    )
}

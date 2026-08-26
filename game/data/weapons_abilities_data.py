from ability_module import Ability
from systems.effect_module import DamageEffect, DotEffect


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
                damage=2,
                interval=1.0,
                duration=5.0
            )
        ]
    ),
    "bash": Ability(
        ability_id="bash",
        name="Bash",
        tooltip="Hit the target with the hilt of your weapon for X damage.",
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
    )
}

from .comp_types import Mount, Mount_Faced
from .customizations import cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c, \
    cust_mnt_fire_control_d, cust_mnt_gun_shield, cust_mnt_modular, cust_mnt_pop_up

# TODO: remove fire control from customizations (actually a weapon customization)

mnt_fixed = Mount_Faced(
    "Fixed Mount",
    v_spaces=(0, 3),
    m_spaces=(0, 2),
    cost=0,
    wep_space_cost=0,
    max_spaces=0,
    desc="A fixed mount is a rigid support for a weapon, with no ability to traverse or change its aim point relative "
         "to the vehicle it is attached to. Most fixed mounts face forward and are activated by the pilot or driver, "
         "though there is no mechanical reason why they cannot be mounted in any direction.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up),
    poss_weapons=0
)

mnt_pintle = Mount_Faced(
    "Pintle Mount",
    m_spaces=(2, 0),
    cost=250,
    desc="A pintle mount is simply a post with the weapon fixed upon it. A pintle mount allows the traveller to pivot "
         "the weapon across an entire fire arc. A pintle mount does not necessarily require a separate gunner to fire.",
    facing="Front",
    poss_customizations=(cust_mnt_gun_shield, cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up)
)

mnt_ring = Mount(
    "Ring Mount",
    m_spaces=(2, 0),
    cost=750,
    desc="A ring mount is a rotating mount typically found near or about a hatch. A ring mount requires a separate "
         "gunner to operate.",
    crew=1,
    poss_customizations=(cust_mnt_gun_shield, cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up)
)

mnt_gun_port = Mount_Faced(
    "Gun Port",
    cost=250,
    poss_weapons=2,
    facing="Right",
    desc="A gun port is a small slot with an armored hatch in a particular fire arc that allows a Traveller inside the "
         "vehicle to use a handgun, SMG, or rifle to attack targets outside.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up)
)

mnt_bay = Mount(
    "Bay",
    v_spaces=(0, 3),
    m_spaces=(0, 2),
    wep_space_cost=2500,
    desc="A bay is an internal space designed to hold one-shot ordnance such as bombs, missiles, and torpedoes. It can"
         "only fire one weapon per round.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up),
    poss_weapons=1
)


mnt_multibay = Mount(
    "Multi-bay",
    v_spaces=(0, 3),
    m_spaces=(0, 2),
    wep_space_cost=5000,
    desc="A multi-bay is an internal space designed to hold one-shot ordnance such as bombs, missiles, and torpedoes. "
         "It can fire any number of weapons each round.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up),
    poss_weapons=1
)

mnt_hardpoint = Mount(
    "Hardpoint",
    m_spaces=(0, 2),
    wep_space_cost=2000,
    max_spaces=(0, 1),
    desc="A hardpoint is an external mounting point for one-shot ordnance such as bombs and missiles. The main benefit "
         "of hardpoints is that, unlike a bay, any weapons mounted upon them do not consume spaces inside the vehicle.",
    poss_weapons=1,
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_modular, cust_mnt_pop_up)
)

mnt_small_turret = Mount(
    "Small Turret",
    v_spaces=(1, 0),
    m_spaces=(4, 0),
    wep_space_cost=10000,
    desc="A small turret is a simple pod that contains only the weapon and any electronics required to fire it, "
         "controlled from a remote station within the vehicle. It is able to fire into any arc.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_pop_up, cust_mnt_modular)
)

mnt_large_turret = Mount(
    "Large Turret",
    v_spaces=(4, 1),
    m_spaces=(0, 1),
    wep_space_cost=25000,
    desc="A large turret can mount much bulkier weapons and has enough space within for crew to operate it. It is "
         "considered an integral part of a vehicle, as opposed to a small turret.",
    poss_customizations=(cust_mnt_fire_control_a, cust_mnt_fire_control_b, cust_mnt_fire_control_c,
                         cust_mnt_fire_control_d, cust_mnt_pop_up, cust_mnt_modular)
)

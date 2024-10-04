from .comp_types import Customization, Customization_Plane, Customization_Airship, Customization_Mount

# chassis customizations
# light ground vehicles
cust_chas_open_frame_a = Customization(
    "Open Frame",
    agility=1,
    max_spaces=3,
    cost=(750, 4, 0),
    speed=(1, 0, 0),
    desc="An open frame vehicle is a light ground vehicle that the rider mounts rather than climbs inside. They often "
         "have just two or three wheels to make a motorcycle or trike.",
    traits=("Open Vehicle")
)

cust_chas_monowheel = Customization(
    "Monowheel",
    tech_level=9,
    agility=2,
    max_spaces=3,
    cost=(2500, 4, 0),
    speed=(1, 0, 0),
    desc="A development of the motorcycle, this vehicle uses complex gyroscopic systems to balance itself on a single "
         "wheel.",
    traits=("Open Vehicle")
)

cust_chas_rail_rider_a = Customization(
    "Rail Rider",
    agility=-2,
    speed=(1, 0, 0),
    spaces=(1, 0, 2),
    cost=(400, 4, 0),
    desc="A Light Ground Vehicle can be designed to run on a rail network, either exclusively or in addition to "
         "another mode of travel. This consumes 0 Spaces unless the vehicle is designed to run off of rails, in which "
         "case it consumes 1 Space.")

cust_chas_rough_terrain_a = Customization(
    "Rough Terrain",
    cost=(100, 4, 0),
    desc="A Light Ground Vehicle can have its suspension and drive systems modified to handle rough terrain.",
    traits=("Off-roader")
)

cust_chas_all_terrain_a = Customization(
    "All-terrain Vehicle",
    cost=(250, 4, 0),
    desc="A Light Ground Vehicle can have its suspension and drive systems modified and additional wheels added to "
         "improve its handling in rough terrain.",
    traits=("ATV")
)

cust_chas_tracks_a = Customization(
    "Tracks",
    tech_level=5,
    skill="Drive (tracks)",
    cost=(750, 4, 0),
    speed=(-1, 0, 0),
    desc="A Light Ground Vehicle can be built with tracks instead of wheels, specializing it to handle difficult "
         "terrain at the expense of road performance.",
    traits=("Tracked")
)

# heavy ground vehicles
cust_chas_armored_fighting_vehicle_a = Customization(
    "Armored Fighting Vehicle",
    tech_level=5,
    cost=(3000, 4, 0),
    speed=(-1, 0, 0),
    desc="Turning a Heavy Ground Vehicle into an Armored Fighting Vehicle (AFV) requires adding structural support, "
         "armor, and off-road capability.",
    traits=["AFV", "Off-roader"]
)

cust_chas_rail_rider_b = Customization(
    "Rail Rider",
    agility=-2,
    cost=(1000, 4, 0),
    speed=(1, 0, 0),
    spaces=(1, 0, 2),
    desc="A Heavy Ground Vehicle can be design to run on a rail network, either exclusively or in addition to another "
         "mode of travel. This consumes 0 Spaces unless the vehicle is designed to run off of rails, in which case it "
         "consumes 1 Space."
)

cust_chas_rough_terrain_b = Customization(
    "Rough Terrain",
    cost=(500, 4, 0),
    desc="A Heavy Ground Vehicle can have its suspension and drive systems modified to handle rough terrain.",
    traits=("Off-roader")
)

cust_chas_all_terrain_b = Customization(
    "All-terrain Vehicle",
    cost=(1000, 4, 0),
    desc="A Heavy Ground Vehicle can have its suspension and drive systems modified and additional wheels added to "
         "improve its handling in rough terrain.",
    traits=("ATV")
)

cust_chas_tracks_b = Customization(
    "Tracks",
    tech_level=5,
    skill="Drive (tracks)",
    cost=(2000, 4, 0),
    speed=(-1, 0, 4),
    desc="A Heavy Ground Vehicle can be built with tracks instead of wheels, specializing it to handle difficult "
         "terrain at the expense of performance on roads.",
    traits=("Tracked")
)

cust_chas_tunneller = Customization(
    "Tunneller",
    tech_level=7,
    skill="Drive (mole)",
    cost=(25000, 4, 0),
    speed=(-1, 0, 0),
    desc="By mounting large drills or other boring equipment to a Heavy Ground Vehicle, it can be turned into a "
         "tunnelling machine capable of moving through solid rock. While travelling through rock, it moves 10 meters "
         "per hour, multiplied by its Tech Level (e.g., TL 10 = 100 meters per hour)."
)

# light grav vehicles
cust_chas_open_frame_b = Customization(
    "Open Frame",
    agility=1,
    max_spaces=3,
    cost=(10000, 4, 0),
    speed=(1, 0, 0),
    desc="The smallest Light Grave Vehicles can be built as an open frame with passengers effectively sitting on top "
         "or astride it. The g/bike is a good example of such a vehicle. They tend to be extremely fast but, without "
         "adequate computer-assisted controls, utterly lethal.",
    traits=("Open Vehicle")
)

cust_chas_streamlined_a = Customization(
    "Streamlined",
    agility=1,
    cost=(30000, 4, 0),
    speed=(1, 0, 0),
    desc="High performance grav vehicles can be designed with aerodynamic hulls that allow them to travel at much "
         "greater speeds."
)

# heavy grav vehicles
cust_chas_armored_fighting_vehicle_b = Customization(
    "Armored Fighting Vehicle",
    cost=(100000, 4, 0),
    speed=(-1, 0, 0),
    desc="A natural progression from wheeled and tracked-based combat vehicles, grav vehicles make extremely good "
         "weapons platforms for any military, crossing the boundaries between tanks and attack aircraft.",
    traits=("AFV")
)

cust_chas_streamlined_b = Customization(
    "Streamlined",
    cost=(50000, 4, 0),
    speed=(1, 0, 0),
    desc="High performance grav vehicles can be designed with aerodynamic hulls that allow them to travel at much "
         "greater speeds."
)

# unpowered ground vehicle
cust_chas_wind_powered = Customization(
    "Wind-powered",
    tech_level=3,
    tech_table={1: (2, 0), 7: (3, 0), 10: (4, 0)},
    cost=(200, 4, 0),
    desc="By using sails more commonly seen on waterborne vehicles, a light chassis can be propelled at some "
         "surprising speed. However, the vehicle is utterly reliant on prevailing conditions and its maximum speed can "
         "never exceed that of the current wind."
)

# unpowered boat
cust_chas_outboard_motor_a = Customization(
    "Light Outboard Motor",
    tech_level=3,
    cost=(100, 4, 0),
    desc="For the convenience of the crew, a light outboard motor can be fitted to a rowed or sailing boat. These "
         "propel a craft at a minimum of Idle speed and have a range of 100km."
)

cust_chas_outboard_motor_b = Customization(
    "Heavy Outboard Motor",
    tech_level=3,
    cost=(250, 4, 0),
    desc="For the convenience of the crew, a heavy outboard motor can be fitted to a rowed or sailing boat. These "
         "propel a craft at a minimum of Very Slow speed and have a range of 100km."
)

# powered boat
cust_chas_hydrofoil_a = Customization(
    "Hydrofoil",
    cost=(4000, 4, 0),
    speed=(1, 0, 0),
    desc="Hydrofoils attached to the underside of a boat's hull allow it to rise out of the water when accelerating, "
         "reducing friction with the water and permitting greater speeds."
)

# ship
cust_chas_hydrofoil_b = Customization(
    "Hydrofoil",
    cost=(8000, 4, 0),
    speed=(1, 0, 0),
    desc="Hydrofoils attached to the underside of a ship's hull allow it to rise out of the water when accelerating, "
         "reducing friction with the water and permitting greater speeds."
)

# general submersible
cust_chas_increased_dive = Customization(
    # this one needs a special rule that I don't think is easy to elucidate here (see readme notes [2])
    "Increased Dive",
    cost=(2, 3, 1),
    desc="By increasing the submersible’s structural strength, it can be made to dive deeper without fear of being "
         "crushed by the surrounding water. For every 100% increase in the submersible’s Cost per Space, its Armor, "
         "Safe and Crush Depths are increased by 100%."

)

# light submersible
cust_chas_supercavitating_drive_a = Customization(
    # this might require a special rule(s) that I don't know how to elucidate here, yet (min_spaces = 10, diff tech
    # levels, etc.)
    "Supercavitating Drive A",
    tech_level=8,
    spaces=(0.4, 1, 0),
    speed=(7, 1, 0),
    cost=(200000, 4, 0),
    range=(700, 1),
    this_min_spaces=10,
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_b = Customization(
    "Supercavitating Drive B",
    tech_level=10,
    spaces=(0.3, 1, 0),
    speed=(7, 1, 0),
    cost=(100000, 4, 0),
    range=(1600, 1),
    this_min_spaces=10,
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_c = Customization(
    "Supercavitating Drive C",
    tech_level=12,
    spaces=(0.2, 1, 0),
    speed=(8, 1, 0),
    range=(1800, 1),
    this_min_spaces=10,
    cost=(50000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_d = Customization(
    "Supercavitating Drive D",
    tech_level=14,
    spaces=(0.1, 1, 0),
    speed=(8, 1, 0),
    range=(2000, 1),
    this_min_spaces=10,
    cost=(25000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

# heavy submersible
cust_chas_supercavitating_drive_e = Customization(
    "Supercavitating Drive A",
    tech_level=8,
    spaces=(0.4, 1, 0),
    speed=(7, 1, 0),
    range=(700, 1),
    this_min_spaces=10,
    cost=(500000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_f = Customization(
    "Supercavitating Drive B",
    tech_level=10,
    spaces=(0.3, 1, 0),
    speed=(7, 1, 0),
    range=(1600, 1),
    this_min_spaces=10,
    cost=(400000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_g = Customization(
    "Supercavitating Drive C",
    tech_level=12,
    spaces=(0.2, 1, 0),
    speed=(8, 1, 0),
    range=(1800, 1),
    this_min_spaces=10,
    cost=(250000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

cust_chas_supercavitating_drive_h = Customization(
    "Supercavitating Drive D",
    tech_level=14,
    spaces=(0.1, 1, 0),
    speed=(8, 1, 0),
    range=(2000, 1),
    this_min_spaces=10,
    cost=(100000, 4, 0),
    desc="While most submersibles are propelled by props or water jets, a supercavitating drive surrounds the craft "
         "with a bubble of atmosphere and propels it forward through the use of rockets, jets, or thrusters. By "
         "eliminating the friction of the water surrounding it, the supercavitating drive is capable of driving the "
         "submersible forward at very high speeds. Requires a minimum of 10 Spaces."
)

# airship
cust_chas_lifting_body = Customization_Airship(
    "Lifting Body",
    tech_level=7,
    spaces=(100, 0, 1),
    cost=(1000, 4, 0),
    speed=(1, 0, 0),
    # this is added
    avail_spaces=0.1,
    desc="This is a hybrid aircraft, combining rigid wings and a lift-generating fuselage with a gas envelope which, "
         "in itself, is capable of supporting the entire craft. This is, in a way, the best of both worlds, providing "
         "a massive lifting capability with increased speed. Additionally, a lifting body airship has 20% of its "
         "Spaces available for crew and customization."
)

# light aeroplane
cust_chas_floats_a = Customization_Plane(
    "Floats",
    agility=-1,
    cost=(1500, 4, 0),
    speed=(-1, 0, 0),
    desc="By adding floats, pontoons, or shaping the fuselage, an aeroplane can be given the ability to land on water."
)

cust_chas_folding_wings_a = Customization_Plane(
    "Folding Wings",
    tech_level=4,
    cost=(3000, 4, 0),
    shipping=(-0.25, 0),
    desc="Aeroplanes can be designed with folding wings, tail, and props in order for them to be stored more "
         "efficiently, either for shipping or within a busy hangar."
)

cust_chas_stol_a = Customization_Plane(
    "Short Take-off/Landing",
    cost=(5000, 4, 0),
    airstrip=0.5,
    desc="The ability to perform Short Take-offs and Landings is typically achieved through the use of high-lift "
         "devices and revised aerofoils. This allows the aeroplane to take-off and land in half the normal distance."
)

cust_chas_tilt_rotors_a = Customization_Plane(
    "Tilt Rotors",
    cost=(15000, 4, 0),
    speed=(-1, 0, 0),
    airstrip=0.0,
    desc="Tilt rotors (or ducted fans), typically placed on the wingtips, allow an aeroplane to take-off and land "
         "vertically, as if it were a helicopter. Once height has been gained, the rotors tilt forward to provide "
         "forward motion. This eliminates the need for an airstrip."
)

# heavy aeroplane
cust_chas_floats_b = Customization_Plane(
    "Floats",
    agility=-1,
    cost=(3000, 4, 0),
    speed=(-1, 0, 0),
    desc="By adding floats, pontoons, or shaping the fuselage, an aeroplane can be given the ability to land on water."
)

cust_chas_folding_wings_b = Customization_Plane(
    "Folding Wings",
    tech_level=4,
    cost=(6000, 4, 0),
    shipping=(-0.25, 0),
    desc="Aeroplanes can be designed with folding wings, tail, and props in order for them to be stored more "
         "efficiently, either for shipping or within a busy hangar."
)

cust_chas_stol_b = Customization_Plane(
    "Short Take-off/Landing",
    cost=(7500, 4, 0),
    airstrip=0.5,
    desc="The ability to perform Short Take-offs and Landings is typically achieved through the use of high-lift "
         "devices and revised aerofoils. This allows the aeroplane to take-off and land in half the normal distance."
)

cust_chas_tilt_rotors_b = Customization_Plane(
    "Tilt Rotors",
    cost=(25000, 4, 0),
    speed=(-1, 0, 0),
    airstrip=0.0,
    desc="Tilt rotors (or ducted fans), typically placed on the wingtips, allow an aeroplane to take-off and land "
         "vertically, as if it were a helicopter. Once height has been gained, the rotors tilt forward to provide "
         "forward motion. This eliminates the need for an airstrip."
)

# generic jet
cust_chas_floats_c = Customization_Plane(
    "Floats",
    cost=(10000, 4, 0),
    speed=(-1, 0, 0),
    desc="By shaping the fuselage, a Light Jet can be given the ability to land on water."
)

# light jet
cust_chas_folding_wings_c = Customization_Plane(
    "Folding Wings",
    tech_level=5,
    cost=(12500, 4, 0),
    shipping=(-0.25, 0),
    desc="Light Jets can be designed with folding wings and tail in order for them to be stored more efficiently, "
         "either for shipping or within a busy hangar."
)

cust_chas_stol_c = Customization_Plane(
    "Short Take-off/Landing",
    cost=(25000, 4, 0),
    airstrip=0.5,
    desc="The ability to perform Short Take-offs and Landings is typically achieved through the use of high-lift "
         "devices and revised aerofoils. This allows the Light Jet to take-off and land in half the normal distance."
)

cust_chas_supersonic_a = Customization_Plane(
    "Supersonic",
    cost=(100000, 4, 0),
    speed=(9, 1, 0),
    desc="Light Jets can be designed to achieve supersonic speeds."
)

cust_chas_tilt_jets_a = Customization_Plane(
    "Tilt Jets",
    cost=(50000, 4, 0),
    airstrip=0.0,
    desc="Rotating jet nozzles allow a Light Jet to take-off and land vertically, as if it were a helicopter. Once "
         "height has been gained, the jets tilt forward to provide forward motion. This eliminates the need for an "
         "airstrip."
)

# heavy jet
cust_chas_folding_wings_d = Customization_Plane(
    "Folding Wings",
    tech_level=5,
    cost=(15000, 4, 0),
    shipping=(-0.25, 0),
    desc="Heavy Jets can be designed with folding wings and tail in order for them to be stored more efficiently, "
         "either for shipping or within a busy hangar."
)

cust_chas_stol_d = Customization_Plane(
    "Short Take-off/Landing",
    cost=(30000, 4, 0),
    airstrip=0.5,
    desc="The ability to perform Short Take-offs and Landings is typically achieved through the use of high-lift "
         "devices and revised aerofoils. This allows the Heavy Jet to take-off and land in half the normal distance."
)

cust_chas_supersonic_b = Customization_Plane(
    "Supersonic",
    cost=(200000, 4, 0),
    speed=(9, 1, 0),
    desc="Heavy jets can be designed to achieve supersonic speeds."
)

cust_chas_tilt_jets_b = Customization_Plane(
    "Tilt Jets",
    cost=(75000, 4, 0),
    airstrip=0.0,
    desc="Rotating jet nozzles allow a Heavy Jet to take-off and land vertically, as if it were a helicopter. Once "
         "height has been gained, the jets tilt forward to provide forward motion. This eliminates the need for an "
         "airstrip."
)

# vtol
cust_chas_aerodyne = Customization(
    "Aerodyne",
    tech_level=7,
    shipping=(0.5, 1),
    cost=(10000, 4, 0),
    speed=(1, 0, 0),
    desc="A helicopter can instead be designed as an aerodyne, a type of VTOL aircraft kept aloft by the power of its "
         "jet engines alone."
)

cust_chas_floats_d = Customization(
    "Floats",
    cost=(5000, 4, 0),
    speed=(-1, 0, 0),
    desc="By adding floats, pontoons, or shaping the fuselage, a helicopter can be given the ability to land on water."
)

cust_chas_folding_wings_e = Customization(
    "Folding Wings/Rotors",
    cost=(2500, 4, 0),
    shipping=(-0.5, 0),
    desc="Helicopters can be designed with folding tail and rotor (and ornithopter with folding wings and fins) in "
         "order for them to be stored more efficiently, either for shipping or for storage within a busy hangar."
)

# light walker
cust_chas_multi_legs_a = Customization(
    "Multi-legs",
    agility=1,
    cost=(10000, 4, 0),
    desc="Walkers are assumed to have two legs, but some sport multi-legged designs intended to balance their weight "
         "and make the walker easier to control."
)

# heavy walker
cust_chas_armored_fighting_vehicle_c = Customization(
    "Armored Fighting Vehicle",
    cost=(20000, 4, 0),
    speed=(-1, 0, 0),
    desc="Turning a Heavy Walker into an Armored Fighting Vehicle (AFV) requires adding structural support and armor, "
         "but can make for a terrifying war machine.",
    traits=("AFV")
)

cust_chas_multi_legs_b = Customization(
    "Multi-legs",
    agility=1,
    cost=(20000, 4, 0),
    desc="Walkers are assumed to have two legs, but some sport multi-legged designs intended to balance their weight "
         "and make the walker easier to control."
)

# light hovercraft
cust_chas_open_frame_c = Customization(
    "Open Frame",
    agility=1,
    max_spaces=3,
    cost=(2500, 4, 0),
    speed=(1, 0, 0),
    desc="An open frame vehicle is a Hovercraft that the rider mounts rather than climbs inside.",
    traits=("Open Vehicle")
)

# heavy hovercraft
cust_chas_armored_fighting_vehicle_d = Customization(
    "Armored Fighting Vehicle",
    tech_level=5,
    cost=(10000, 4, 0),
    speed=(-1, 0, 0),
    desc="Turning a Hovercraft into an Armored Fighting Vehicle (AFV) requires adding structural support and armor.",
    traits=("AFV")
)


# TODO:
# performance customizations


# TODO:
# control systems customizations


# TODO:
# drive systems customizations


# TODO:
# power systems customizations


# TODO:
# active defense customizations


# TODO:
# electronics customizations


# TODO:
# stealth and camo customizations


# TODO:
# environmental customizations


# TODO:
# utility customizations


# TODO:
# mount customizations
# TODO: fire control customization is actually a weapon customization
cust_mnt_fire_control_a = Customization_Mount(
    "Basic Fire Control System",
    tech_level=6,
    cost=(10000, 0, 0),
    spaces=(0, 0, 0),
    desc="The use of fire control systems allows weapons to be targeted far more accurately. This can range from "
         "simple gyrostabilization to laser-rangefinders and integration of the vehicle's own advanced sensor arrays "
         "to the weapon systems. However, due to their cost and complexity, fire control systems are normally fitted "
         "only to a vehicle's primary weapons.\n\n"
         "All fire control systems grant the Scope trait to the weapon they are attached to (p. 133, Traveller Core "
         "Rulebook).",
    dice_mod="+1 Attack Roll DM",
    traits=("Scope")
)

cust_mnt_fire_control_b = Customization_Mount(
    "Improved Fire Control System",
    tech_level=8,
    cost=(25000, 0, 0),
    spaces=(0, 0, 0),
    desc="The use of fire control systems allows weapons to be targeted far more accurately. This can range from "
         "simple gyrostabilization to laser-rangefinders and integration of the vehicle's own advanced sensor arrays "
         "to the weapon systems. However, due to their cost and complexity, fire control systems are normally fitted "
         "only to a vehicle's primary weapons.\n\n"
         "All fire control systems grant the Scope trait to the weapon they are attached to (p. 133, Traveller Core "
         "Rulebook).",
    dice_mod="+2 Attack Roll DM",
    traits=("Scope")
)

cust_mnt_fire_control_c = Customization_Mount(
    "Enhanced Fire Control System",
    tech_level=10,
    cost=(25000, 0, 0),
    spaces=(0, 0, 0),
    desc="The use of fire control systems allows weapons to be targeted far more accurately. This can range from "
         "simple gyrostabilization to laser-rangefinders and integration of the vehicle's own advanced sensor arrays "
         "to the weapon systems. However, due to their cost and complexity, fire control systems are normally fitted "
         "only to a vehicle's primary weapons.\n\n"
         "All fire control systems grant the Scope trait to the weapon they are attached to (p. 133, Traveller Core "
         "Rulebook).",
    dice_mod="+3 Attack Roll DM",
    traits=("Scope")
)

cust_mnt_fire_control_d = Customization_Mount(
    "Advanced Fire Control System",
    tech_level=12,
    cost=(25000, 0, 0),
    spaces=(0, 0, 0),
    desc="The use of fire control systems allows weapons to be targeted far more accurately. This can range from "
         "simple gyrostabilization to laser-rangefinders and integration of the vehicle's own advanced sensor arrays "
         "to the weapon systems. However, due to their cost and complexity, fire control systems are normally fitted "
         "only to a vehicle's primary weapons.\n\n"
         "All fire control systems grant the Scope trait to the weapon they are attached to (p. 133, Traveller Core "
         "Rulebook).",
    dice_mod="+4 Attack Roll DM",
    traits=("Scope")
)


cust_mnt_gun_shield = Customization(
    "Gun Shield",
    tech_level=1,
    cost=(1000, 0, 0),
    spaces=(0, 0, 0),
    desc="A plate which provides a Traveller protection equal to the vehicle's Tech Level in the direction of the "
         "mount's facing."
)

cust_mnt_pop_up = Customization(
    "Pop-up Mount",
    desc="Any mount can be concealed within a vehicle until required. This is typically done in order to gain surprise "
         "on an enemy or to avoid cursory checks from discovering illegal weaponry.",
    cost=(10000, 4, 0),
    spaces=(1, 4),
    this_min_spaces=1,
)

cust_mnt_modular = Customization(
    "Modular Mount",
    desc="Any mount can be made modular, allowing a variety of weapons to be fitted. This allows a vehicle to change "
         "its 'mission profile' and become effective against different enemies.\n\n"
         "Changing a weapon on a modular mount requires a Routine (6+) Mechanics check (1D minutes, INT or EDU).",
    cost=(1.5, 5, 0)
)

# not sure how to do this one yet
# cust_mnt_linked = Customization_Mount()

# weapon customizations

cust_wep_ammunition = Customization(
    "Ammunition",
    desc="Additional Spaces set aside for ammunition allows an extra magazine (as defined by the weapon) to be "
         "directly attached to a weapon, allowing it to be used without the need to reload. These Spaces have no cost "
         "other than the ammunition that fills them. Weapons of less than 1 ton may have up to 10 magazines for every "
         "Space dedicated to ammunition in this way.",
    spaces=(0, 0, 1),
)


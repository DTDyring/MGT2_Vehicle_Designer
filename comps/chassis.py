from .comp_types import Chassis, Chassis_Plane, Chassis_Airship, Chassis_Submersible
from .customizations import *

light_ground_vehicle = Chassis(
    "Light Ground Vehicle",
    tech_level=4,
    max_spaces=20,
    cost=750,
    hull=(2.0, 1),
    shipping=0.5,
    skill="Drive (wheel)",
    desc="Light Ground Vehicles are prolific on industrialized worlds as they emerge into technological adolescence. "
         "They are typically used for individual or group transportation, such as with the ubiquitous family car, and "
         "quickly become commonplace for all but the very poor. Because of their low cost, Light Ground Vehicles can "
         "still be found on worlds with a higher base of technology where anti-grav vehicles should otherwise have "
         "rendered them obsolete.",
    tech_table={
        4: (2, 100), 5: (3, 200), 7: (4, 400), 9: (5, 500), 11: (6, 600)
    },
    poss_customizations=(
        cust_chas_open_frame_a, cust_chas_monowheel, cust_chas_rail_rider_a, cust_chas_rough_terrain_a,
        cust_chas_all_terrain_a, cust_chas_tracks_a
        )
)

heavy_ground_vehicle = Chassis(
    "Heavy Ground Vehicle",
    tech_level=4,
    min_spaces=20,
    cost=3000,
    hull=(3.0, 1),
    shipping=0.5,
    skill="Drive (wheel)",
    desc="Heavy Ground Vehicles are almost as common as their smaller counterparts on industrialized worlds. They are "
         "typically used for mass and heavy transportation, of both goods and people. Heavy Ground Vehicles start with "
         "a typical four-wheel layout but rapidly add more as their size increases.",
    tech_table={
        4: (2, 100), 5: (3, 200), 7: (4, 400), 9: (4, 500), 11: (6, 600)
    },
    poss_customizations=(
        cust_chas_armored_fighting_vehicle_a, cust_chas_rail_rider_b, cust_chas_rough_terrain_b,
        cust_chas_all_terrain_b, cust_chas_tracks_b, cust_chas_tunneller
    )
)

light_grav_vehicle = Chassis(
    "Light Grav Vehicle",
    tech_level=8,
    agility=1,
    max_spaces=20,
    cost=30000,
    hull=(2.0, 1),
    shipping=0.5,
    skill="Flyer (grav)",
    desc="Once grav technology becomes cheap and widely available, most worlds make a rapid transition from ground to"
         "grav vehicles. In just about every measurable way, grav vehicles are better, being faster, smoother, and "
         "safer.",
    tech_table={
        8: (5, 1000), 9: (6, 2000), 11: (6, 3000), 13: (7, 4000), 15: (7, 5000)
    },
    poss_customizations=(
        cust_chas_open_frame_b, cust_chas_streamlined_a
    )
)

heavy_grav_vehicle = Chassis(
    "Heavy Grav Vehicle",
    tech_level=8,
    agility=-1,
    min_spaces=20,
    cost=80000,
    hull=(2.0, 1),
    shipping=0.5,
    skill="Flyer (grav)",
    desc="With ultra-heavy duty grav thrusters, even large vehicles can become airborne. This inevitably leads to a "
         "revolution in transportation across many worlds, as expensive aircraft are replaced by ever larger grav "
         "vehicles.",
    tech_table={
        8: (5, 1000), 9: (6, 2000), 11: (6, 3000), 13: (6, 4000), 15: (7, 5000)
    },
    poss_customizations=(
        cust_chas_armored_fighting_vehicle_b, cust_chas_streamlined_b
    )
)

unpowered_vehicle = Chassis(
    "Unpowered Vehicle",
    tech_level=1,
    agility=-1,
    max_spaces=10,
    cost=100,
    hull=(1.0, 1),
    shipping=0.5,
    skill="Drive (wheel)",
    desc="These vehicles do not possess a motive system of their own and rely on the muscles of beasts of burden (as "
         "in the case of a cart or wagon) or their own crew (such as a rickshaw or bicycle). Clever mechanics can "
         "increase the speed of the vehicle beyond that of its occupants on foot, but if it is being pushed or pulled, "
         "its speed can never exceed that of the creatures' own movement.",
    tech_table={
        1: (2, 0), 7: (3, 0), 10: (3, 0)
    },
    poss_customizations=(
        cust_chas_wind_powered
    )
)

unpowered_boat = Chassis(
    "Unpowered Boat",
    tech_level=1,
    agility=-1,
    cost=150,
    hull=(1.0, 1),
    shipping=0.25,
    skill="Seafarer(personal or sail)",
    desc="Ships and boats provide the best means to transport people and cargo long distances wherever seas or rivers "
         "are present. Such craft can be powered by rowers on board and while this makes the vessel largely immune to "
         "the effects of wind, those that utilize sails are far more efficient. The possible speeds listed assume "
         "fresh crews and benevolent winds, and can be lowered by the referee to reflect adverse conditions. Range is "
         "effectively limited only by the food and supplies which the craft can carry.",
    tech_table={
        4: (2, 200), 5: (3, 300), 7: (4, 400), 9: (5, 500), 11: (6, 600)
    },
    poss_customizations=(
        cust_chas_outboard_motor_a, cust_chas_outboard_motor_b
    )
)

powered_boat = Chassis(
    "Powered Boat",
    tech_level=3,
    agility=-2,
    min_spaces=5,
    max_spaces=50,
    cost=2000,
    hull=(2.0, 1),
    shipping=0.5,
    skill="Seafarer(personal)",
    desc="Boats are a common sight on the rivers and coastlines of any civilized world and, due to their cheapness and "
         "utility, remain viable even when grav vehicles begin appearing. Small boats have a wide variety of "
         "applications, from harvesting the sea and pleasure use, to rescuing stranded seafarers and small-scale "
         "military operations.",
    tech_table={
        3: (1, 100), 4: (2, 200), 6: (3, 400), 9: (3, 800), 12: (4, 1200)
    },
    poss_customizations=(
        cust_chas_hydrofoil_a
    )
)

ship = Chassis(
    "Ship",
    tech_level=4,
    agility=-6,
    min_spaces=50,
    cost=5000,
    hull=(4.0, 1),
    shipping=0.5,
    skill="Seafarer (ocean ship)",
    desc="Ships can reach immense sizes and, until spacecraft appear, are typically the largest vehicles a "
         "civilization will build. They are used chiefly to haul vast quantities of cargo across the ocean but readily "
         "serve as passenger liners and military vessels.",
    tech_table={
        4: (2, 2000), 5: (2, 4000), 7: (3, 6000), 9: (3, 8000), 11: (4, 12000)
    },
    poss_customizations=(
        cust_chas_hydrofoil_b
    )
)

light_submersible = Chassis_Submersible(
    "Light Submersible",
    tech_level=4,
    agility=-2,
    max_spaces=20,
    cost=50000,
    hull=(3.0, 1),
    shipping=0.5,
    skill="Seafarer (Submarine)",
    desc="A submersible is a water-going craft that can submerge beneath the surface, while a submarine is a craft "
         "designed to remain under the surface for the greater part of its life, but is capable of surface travel. "
         "Small versions of both have wide-ranging applications in civilian life, though specialized military models "
         "also exist.\n\n"
         "Submersibles have not only a Speed and Range, but also a Safe Depth (the depth to which they can usually "
         "dive), a Crush Depth (the depth to which they can go before being automatically destroyed), and Life Support "
         "(how many days a submersible can support its crew without resurfacing for air). All submersibles have the "
         "Life Support and Hostile Environment Customizations (p. 55, Vehicle Handbook).",
    tech_table={
        4: (1, 50), 6: (2, 100), 9: (3, 150), 12: (4, 200), 15: (4, 250)
    },
    sub_table={
        4: (50, 150, 50), 6: (200, 600, 100), 9: (600, 1800, 200), 12: (2000, 6000, 400), 15: (4000, 12000, 0)
    },
    poss_customizations=(
        cust_chas_increased_dive, cust_chas_supercavitating_drive_a, cust_chas_supercavitating_drive_b,
        cust_chas_supercavitating_drive_c, cust_chas_supercavitating_drive_d
    )
)

heavy_submersible = Chassis_Submersible(
    "Heavy Submersible",
    tech_level=4,
    agility=-4,
    min_spaces=20,
    cost=100000,
    hull=(3.0, 1),
    shipping=0.5,
    skill="Seafarer (submarine)",
    desc="Heavy submersibles can reach the size of many of the ships they sail beneath and while some are used for "
         "carrying cargo, especially on worlds that have a hostile or dangerous atmosphere, most have military "
         "applications. These can be highly advanced war machines, packing extremely powerful weaponry and "
         "state-of-the-art stealth systems.\n\n"
         "Submersibles have not only a Speed and Range, but also a Safe Depth (the depth to which they can usually "
         "dive), a Crush Depth (the depth to which they can go before being automatically destroyed), and Life Support "
         "(how many days a submersible can support its crew without resurfacing for air). All submersibles have the "
         "Life Support and Hostile Environment Customizations (p. 55, Vehicle Handbook).",
    tech_table={
        4: (1, 50), 6: (2, 100), 9: (3, 150), 12: (4, 200), 15: (4, 250)
    },
    sub_table={
        4: (50, 150, 50), 6: (200, 600, 100), 9: (600, 1800, 200), 12: (2000, 6000, 400), 15: (4000, 12000, 0)
    },
    poss_customizations=(
        cust_chas_increased_dive, cust_chas_supercavitating_drive_e, cust_chas_supercavitating_drive_f,
        cust_chas_supercavitating_drive_g, cust_chas_supercavitating_drive_h
    )
)

airship = Chassis_Airship(
    "Airship",
    tech_level=3,
    skill="Flyer (airship)",
    agility=-3,
    min_spaces=10,
    cost=300,
    hull=(1.0, 5),
    shipping=0.1,
    desc="Airships use a gas envelope containing a large volume of lighter-than-air gas (typically helium) to rise "
         "through the air. Engines provide forward motion without having to expend energy to gain height, making an "
         "airship efficient but slow. An airship without engines is a balloon and at the mercy of prevailing winds."
         "\n\n"
         "Airships have a great many Spaces, but most will be consumed by the gas envelope required to lift the craft. "
         "Only 10% of Spaces are available for crew, passengers, and customizations.\n\n"
         "The Tech 3 Speed and Range on the Tech Table assume a low TL hot air balloon.",
    tech_table={
        3: (1, 100), 4: (2, 4000), 6: (4, 6000), 8: (4, 8000), 10: (4, 10000), 12: (4, 12000)
    },
    poss_customizations=(
        cust_chas_lifting_body
    )
)

light_aeroplane = Chassis_Plane(
    "Light Aeroplane",
    tech_level=4,
    skill="Flyer (wing)",
    agility=1,
    max_spaces=10,
    cost=15000,
    hull=(1.0, 2),
    shipping=0.5,
    airstrip=1200,
    desc="These are propeller-driven aircraft that rely on a fixed wing for lift, used widely on pre-gravitic worlds "
         "for personal and short-ranged transportation. Their appearance revolutionizes all aspects of society, from "
         "travel to the military, but the constant need of forward motion to create lift means they are quickly "
         "replaced when grav vehicles appear.",
    tech_table={
        4: (4, 300), 5: (5, 600), 7: (6, 1200), 9: (6, 2400), 11: (7, 4800)
    },
    poss_customizations=(
        cust_chas_floats_a, cust_chas_folding_wings_a, cust_chas_stol_a, cust_chas_tilt_rotors_a
    )
)

heavy_aeroplane = Chassis_Plane(
    "Heavy Aeroplane",
    tech_level=4,
    skill="Flyer (wing)",
    agility=-2,
    min_spaces=10,
    cost=25000,
    hull=(1.0, 2),
    shipping=1,
    airstrip=2400,
    desc="From bombers and military transports, to airliners and cargo planes, heavy aeroplanes provide a relatively "
         "cheap way to transport large quantities of materials (or weapons) across long distances.",
    tech_table={
        4: (3, 1000), 5: (4, 2000), 7: (5, 3000), 9: (6, 4000), 11: (7, 5000)
    },
    poss_customizations=(
        cust_chas_floats_b, cust_chas_folding_wings_b, cust_chas_stol_b, cust_chas_tilt_rotors_b
    )
)

light_jet = Chassis_Plane(
    "Light Jet",
    tech_level=5,
    skill="Flyer (wing)",
    agility=1,
    min_spaces=2,
    max_spaces=20,
    cost=50000,
    hull=(1.0, 3),
    shipping=1,
    airstrip=1800,
    desc="The appearance of jet engines, from turbofans to scramjets and hydrogen-fuelled waveriders, gives aircraft a "
         "massive increase in speed and range. They are noticeably more expensive, but the performance benefits "
         "usually outweigh this, especially in frontline combat or as the playthings of nobles.",
    tech_table={
        5: (5, 750), 6: (6, 2000), 9: (7, 4000), 12: (8, 7000)
    },
    poss_customizations=(
        cust_chas_floats_c, cust_chas_folding_wings_c, cust_chas_stol_c, cust_chas_supersonic_a, cust_chas_tilt_jets_a
    )
)

heavy_jet = Chassis_Plane(
    "Heavy Jet",
    tech_level=5,
    skill="Flyer (wing)",
    agility=-2,
    min_spaces=20,
    cost=75000,
    hull=(1.0, 2),
    shipping=2,
    airstrip=3000,
    desc="Large jets become the pre-eminent way of moving both passengers and cargo in both quantity and speed within "
         "pre-gravitic societies. With suitable investment, they are capable of reaching great speeds, with supersonic "
         "aircraft easily achievable at relatively modest Tech Levels.",
    tech_table={
        5: (5, 1000), 6: (6, 4000), 9: (7, 7000), 12: (8, 10000)
    },
    poss_customizations=(
        cust_chas_floats_c, cust_chas_folding_wings_d, cust_chas_stol_d, cust_chas_supersonic_b, cust_chas_tilt_jets_b
    )
)

vtol = Chassis(
    "Helicopter, Aerodyne, or Ornithopter",
    skill="Flyer (rotor)",
    max_spaces=200,
    cost=25000,
    hull=(1.0, 2),
    shipping=1,
    desc="Helicopters use large diameter rotors (usually a single rotor, though larger helicopters may have two) to "
         "provide both lift and thrust. This is an inefficient method of aerial travel but it does allow helicopters "
         "to take-off and land without the need for a runway. Ornithopters use moving wings to gain lift, which is "
         "even more inefficient, but they sometimes appear due to specific atmospheric conditions or cultural bias. At "
         "higher Tech Levels, aerodynes become possible, using similar principles but replacing the rotor with jet "
         "thrust.",
    tech_table={
        5: (4, 1000), 7: (4, 4000), 9: (5, 7000), 11: (5, 10000)
    },
    poss_customizations=(
        cust_chas_aerodyne, cust_chas_floats_d, cust_chas_folding_wings_e
    )
)

light_walker = Chassis(
    "Light Walker",
    tech_level=8,
    skill="Drive (walker)",
    max_spaces=20,
    cost=10000,
    hull=(2.0, 1),
    shipping=0.5,
    traits=["ATV"],
    desc="Walkers use computer-controlled legs to literally walk, allowing them to negotiate difficult terrain that "
         "would be impassable to wheeled vehicles. They are noticeably larger than suits of powered armor or battle "
         "dress, with even small models requiring a Traveller climbs into them, rather than 'wearing' them.",
    tech_table={
        8: (2, 150), 9: (3, 300), 11: (4, 750), 13: (5, 600), 15: (5, 750)
    },
    poss_customizations=(
        cust_chas_multi_legs_a
    )
)

heavy_walker = Chassis(
    "Heavy Walker",
    tech_level=8,
    skill="Drive (walker)",
    min_spaces=20,
    cost=20000,
    hull=(3.0, 1),
    shipping=0.5,
    traits=["ATV"],
    desc="Larger walkers tend to be very specialized, as their construction is both difficult and expensive. They are "
         "thus used for very specific purposes rather than being designed as general purpose vehicles.",
    tech_table={
        8: (2, 150), 9: (3, 300), 11: (4, 450), 13: (5, 600), 15: (5, 750)
    },
    poss_customizations=(
        cust_chas_armored_fighting_vehicle_c, cust_chas_multi_legs_b
    )
)

light_hovercraft = Chassis(
    "Light Hovercraft",
    tech_level=5,
    skill="Drive (hovercraft)",
    agility=1,
    max_spaces=10,
    cost=10000,
    hull=(1.0, 3),
    shipping=0.5,
    desc="Hovercraft ride on a cushion of air, allowing them to glide over any surface, be it solid or liquid. This "
         "makes them very convenient, especially in less-developed areas, but they are also noisy and lack any great"
         "range.",
    tech_table={
        5: (3, 300), 6: (4, 400), 8: (5, 500), 10: (5, 600), 12: (6, 700)
    },
    poss_customizations=(
        cust_chas_open_frame_c
    )
)

heavy_hovercraft = Chassis(
    "Heavy Hovercraft",
    tech_level=5,
    skill="Drive (hovercraft)",
    min_spaces=10,
    cost=20000,
    hull=(1.0, 2),
    shipping=0.5,
    desc="Larger hovercraft are capable of transporting large loads quickly and easily, and are not dependent on roads "
         "like other ground-based vehicles. They are also more agile than other large vehicles, though they require a "
         "skilled operator to get the best out of them.",
    tech_table={
        5: (3, 300), 6: (4, 400), 8: (5, 500), 10: (5, 600), 12: (6, 700)
    },
    poss_customizations=(
        cust_chas_armored_fighting_vehicle_d
    )
)

from .comp_types import Armor

armor_1 = Armor(
    "Armor A",
    tech_level=0,
    max_armor=10,
    cost=0.05,
    spaces=0.025,
    desc="Wood"
)

armor_2 = Armor(
    "Armor B",
    tech_level=3,
    base_armor=1,
    base_max_armor=15,
    cost=0.03,
    spaces=0.015,
    desc="Iron"
)

armor_3 = Armor(
    "Armor C",
    tech_level=6,
    base_armor=2,
    max_armor=20,
    cost=0.02,
    spaces=0.01,
    desc="Steel, Composites"
)

armor_4 = Armor(
    "Armor D",
    tech_level=9,
    base_armor=3,
    max_armor=30,
    cost=0.01,
    spaces=0.005,
    desc="Crystaliron"
)

armor_5 = Armor(
    "Armor E",
    tech_level=12,
    base_armor=4,
    max_armor=40,
    cost=0.005,
    spaces=0.004,
    desc="Bonded Superdense, Cast Diamond"
)

armor_6 = Armor(
    "Armor F",
    tech_level=15,
    base_armor=4,
    max_armor=50,
    cost=0.0025,
    spaces=0.003,
    desc="Molecular Bonded, Cerametals, Spun Diamond"
)

armor_7 = Armor(
    "Armor G",
    tech_level=18,
    base_armor=5,
    max_armor=60,
    cost=0.001,
    spaces=0.0025,
    desc="Coherent Superdense"
)

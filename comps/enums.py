from enum import Enum
from .customizations import *


class Speed(Enum):
    """Possible vehicle speed bands"""
    # starts at 1 to avoid off-by-one in
    STOPPED = 0
    IDLE = 1
    VERY_SLOW = 2
    SLOW = 3
    MEDIUM = 4
    HIGH = 5
    FAST = 6
    VERY_FAST = 7
    SUBSONIC = 8
    SUPERSONIC = 9
    HYPERSONIC = 10


# maybe don't use this?
class Chas_Customs(Enum):
    open_frame_a = 0
    open_frame_b = 1
    open_frame_c = 2
    monowheel = 3
    rail_rider_a = 4
    rail_rider_b = 5
    rough_terrain_a = 6
    rough_terrain_b = 7
    all_terrain_a = 8
    all_terrain_b = 9
    tracks_a = 10
    tracks_b = 11
    armored_fighting_vehicle_a = 12
    armored_fighting_vehicle_b = 13
    armored_fighting_vehicle_c = 14
    armored_fighting_vehicle_d = 15
    tunneller = 16
    streamlined_a = 17
    streamlined_b = 18
    wind_powered = 19
    outboard_motor_a = 20
    outboard_motor_b = 21
    hydrofoil_a = 22
    hydrofoil_b = 23
    increased_dive = 24
    supercavitating_drive_a = 25
    supercavitating_drive_b = 26
    supercavitating_drive_c = 27
    supercavitating_drive_d = 28
    supercavitating_drive_e = 29
    supercavitating_drive_f = 30
    supercavitating_drive_g = 31
    supercavitating_drive_h = 32
    lifting_body = 33
    floats_a = 34
    floats_b = 35
    floats_c = 36
    floats_d = 37
    folding_wings_a = 38
    folding_wings_b = 39
    folding_wings_c = 40
    folding_wings_d = 41
    folding_wings_e = 42
    stol_a = 43
    stol_b = 44
    stol_c = 45
    stol_d = 46
    tilt_rotors_a = 47
    tilt_rotors_b = 48
    supersonic_a = 49
    supersonic_b = 50
    tilt_jets_a = 51
    tilt_jets_b = 52
    aerodyne = 53
    multi_legs_a = 54
    multi_legs_b = 55


class Cost_Types(Enum):
    """Possible cost types for customizations"""
    FLAT = 0
    PER_SPACE = 1
    PER_10_FULL_SPACES = 2
    PER_CHAS_SPACE_MULT = 3
    PER_CHAS_SPACE_ADD = 4


# maybe don't use this?
class Chassis_Types(Enum):
    """Possible chassis types"""
    LIGHT_GROUND_VEHICLE = 0
    HEAVY_GROUND_VEHICLE = 1
    LIGHT_GRAV_VEHICLE = 2
    HEAVY_GRAV_VEHICLE = 3
    UNPOWERED_VEHICLE = 4
    UNPOWERED_BOAT = 5
    POWERED_BOAT = 6
    SHIP = 7
    LIGHT_SUBMERSIBLE = 8
    HEAVY_SUBMERSIBLE = 9
    AIRSHIP = 10
    LIGHT_AEROPLANE = 11
    HEAVY_AEROPLANE = 12
    LIGHT_JET = 13
    HEAVY_JET = 14
    HELICOPTER = 15
    LIGHT_WALKER = 16
    HEAVY_WALKER = 17
    LIGHT_HOVERCRAFT = 18
    HEAVY_HOVERCRAFT = 19


class Armor_Types(Enum):
    """Named for base protection, list of armor types"""
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Space_Types(Enum):
    """Possible space consumption types"""
    FLAT = 0
    PERCENTAGE = 1
    PER_FULL = 2
    PER_PARTIAL = 3


class Conditionals(Enum):
    FALSE = 0
    is_responsive = 1
    can_off_rail = 2
    is_afv = 3
    not_is_afv = 4
    new_tech_table = 5


class Mount_Arcs(Enum):
    ALL = 0
    FRONT = 1
    LEFT = 2
    RIGHT = 3
    BACK = 4


class Speed_Types(Enum):
    ADD = 0
    REPLACE = 1


class Range_Types(Enum):
    ADD = 0
    REPLACE = 1


class Shipping_Types(Enum):
    ADD = 0
    REPLACE = 1

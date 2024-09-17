from enum import Enum


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


class Cost_Types(Enum):
    """Possible cost types for customizations"""
    FLAT = 0
    PER_SPACE = 1
    PER_10_FULL_SPACES = 2
    PER_PARENT_SPACE_MULT = 3
    PER_PARENT_SPACE_ADD = 4
    FLAT_PARENT_TOTAL_MULT = 5


class Weapon_Types(Enum):
    ALL = 0
    ONE_SHOT = 1
    NONE = 2


class Mount_V_Spaces(Enum):
    FLAT = 0
    FLAT_CREW = 1
    AS_WEAPON_SPACES = 2
    AS_MOUNT_SPACES = 3


class Mount_M_Spaces(Enum):
    FLAT = 0
    AS_WEAPON_SPACES = 1
    RESPONSIVE = 2


class Mount_Max_Spaces(Enum):
    NO_MAX = 0
    QTR_CHAS = 1


class Space_Types(Enum):
    """Possible space consumption/modifier types"""
    FLAT = 0
    PERCENTAGE = 1
    PER_FULL = 2
    PER_PARTIAL = 3
    PARENT_TOTAL_MULT = 4


class Conditionals(Enum):
    FALSE = 0
    is_responsive = 1   # can this be modified by user on the gui
    can_off_rail = 2
    is_afv = 3
    not_is_afv = 4


class Speed_Types(Enum):
    ADD = 0
    REPLACE = 1


class Range_Types(Enum):
    ADD = 0
    REPLACE = 1


class Shipping_Types(Enum):
    ADD = 0
    REPLACE = 1

class Chassis:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.min_tech_level: int = kwargs.pop("tech_level", 0)
        self.min_spaces: int = kwargs.pop("min_spaces", 1)
        self.max_spaces: int = kwargs.pop("max_spaces", 0)
        # hull points per n spaces
        self.hull_to_space: tuple[float, int] = kwargs.pop("hull", (0.0, 0))
        self.shipping_per_space: float = kwargs.pop("shipping", 0.0)
        self.skill: str = kwargs.pop("skill", "N/a")
        self.agility: int = kwargs.pop("agility", 0)
        self.tech_table: dict[int:tuple[int, int]] = kwargs.pop("base_speeds", {}),
        self.trait_list: list[str] = kwargs.pop("traits", [])
        self.cost_per_space: int = kwargs.pop("cost", 0)
        self.description: str = kwargs.pop("desc", "N/a")
        self.possible_customizations: tuple[Customization] = kwargs.pop("poss_customizations", ())
        self.chassis_customizations: list[Customization] = []

        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')


class Chassis_Plane(Chassis):
    def __init__(self, name, /, **kwargs):
        # this is maximum possible airstrip, and should be customizable
        self.airstrip: int = kwargs.pop("airstrip", 0)
        super().__init__(name, **kwargs)


class Chassis_Airship(Chassis):
    def __init__(self, name, /, **kwargs):
        super().__init__(name, **kwargs)
        # this is as a percentage of total spaces in the vehicle
        self.available_spaces: float = 0.1


class Chassis_Submersible(Chassis):
    def __init__(self, name, /, **kwargs):
        self.sub_table: dict[int: tuple[int, int, int]] = kwargs.pop("sub_table", {})
        super().__init__(name, **kwargs)


class Armor:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.min_tech_level: int = kwargs.pop("tech_level", 0)
        self.base_armor: int = kwargs.pop("base_armor", 0)
        self.base_max_armor: int = kwargs.pop("max_armor", 0)
        self.chass_cost_per_point: float = kwargs.pop("cost", 0.0)
        self.spaces_per_point: float = kwargs.pop("spaces", 0.025)
        self.description: str = kwargs.pop("desc", "N/a")
        # TODO: add custom armor facing (poss to vehicle obj)
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')


class Mount:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.vehicle_spaces: int = kwargs.pop("v_spaces", 0)
        self.mount_spaces: int = kwargs.pop("m_spaces", 0)
        self.base_cost: int = kwargs.pop("base_cost", 0)
        self.weapon_space_cost: int = kwargs.pop("wep_space_cost", 0)
        self.mount_arc: int = kwargs.pop("mount_arc", 0)
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')
        self.is_pop_up: bool = False
        self.is_modular: bool = False
        self.crew_complement: int = 0
        self.weapons: list[Weapon] = []


class Customization:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.cost: tuple[int, int, int] = kwargs.pop("cost", (0, 0, 0))
        self.spaces: tuple[int, int, int] = kwargs.pop("spaces", (0, 0, 0))
        self.responsive: int = kwargs.pop("responsive", 0)
        self.max_spaces: int = kwargs.pop("max_spaces", 0)
        self.this_max_spaces: int = kwargs.pop("this_max_spaces", -1)
        self.this_min_spaces: int = kwargs.pop("min_spaces", 0)
        self.speed: tuple[int, int, int] = kwargs.pop("speed", (0, 0, 0))
        self.range: tuple[int, int] = kwargs.pop("range", (0, 0))
        self.shipping: tuple[float, int] = kwargs.pop("shipping", (0.0, 0))
        self.description: str = kwargs.pop("desc", "Lorem ipsum")
        self.traits: list[str] = kwargs.pop("traits", [])
        self.tech_table: dict[int: (int, int)] = kwargs.pop("tech_table", {})
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')


class Customization_Plane(Customization):
    def __init__(self, name, /, **kwargs):
        # this is a multiplier
        self.airstrip: float = kwargs.pop("airstrip", 1.0)
        super().__init__(name, **kwargs)


class Customization_Airship(Customization):
    def __init__(self, name, /, **kwargs):
        # this is additive
        self.available_spaces: float = kwargs.pop("avail_spaces", 0.0)
        super().__init__(name, **kwargs)


class Weapon:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.cost: int = kwargs.pop("cost", 0)
        self.spaces: int = kwargs.pop("spaces", 0)
        self.ammo: int = kwargs.pop("ammo", 0)
        self.range: int = kwargs.pop("range", 0)
        self.damage: str = kwargs.pop("damage", "0")
        self.traits: list[str] = kwargs.pop("traits", [])
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')

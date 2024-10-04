from enums import Cost_Types

class Chassis:
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
        self.traits: tuple[str] = kwargs.pop("traits", ())
        self.cost_per_space: int = kwargs.pop("cost", 0)
        self.description: str = kwargs.pop("desc", "N/a")
        self.possible_customizations: tuple[Customization] = kwargs.pop("poss_customizations", ())
        self.chassis_customizations: list[Customization] = []
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')

    def __repr__(self):
        # TODO: finish this repr
        return (f"CHASSIS_OBJECT: {self.name} | MIN_TL: {self.min_tech_level} | CUR_TL {self.get_tech_level()} | "
                f"MIN_SPC: {self.min_spaces} | MAX_SPC: {self.max_spaces} | BASE_SPC_COST: {self.cost_per_space} | "
                f"CUR_SPC_COST: {self.get_cost_per_space()} | HP_PER_SPACE: {self.hull_to_space} | "
                f"SHPG_TNG: {self.shipping_per_space} | BASE_SKILL: {self.skill} | CUR_SKILL: {self.get_skill} | "
                f"BASE_AGILITY: {self.agility} | CUR_AGILITY: {self.get_agility()} | "
                f"BASE_TECH_TABLE: {self.tech_table} | CUR_TECH_TABLE: {self.get_tech_table()} | "
                f"BASE_TRAITS: {self.traits} | CUR_TRAITS: {self.get_traits()}")

    def get_name(self):
        return self.name

    def get_skill(self):
        """Gets current chassis Skill based on chassis and customizations

        Returns:
            skill: str
        """
        skill = self.skill
        if len(self.chassis_customizations):
            for _ in self.chassis_customizations:
                if _.skill:
                    skill = _.skill
                    break
        else:
            return skill

    def get_tech_level(self):
        high_tl = self.min_tech_level
        if len(self.chassis_customizations):
            for _ in self.chassis_customizations:
                if _.tech_level > high_tl:
                    high_tl = _.tech_level
                else:
                    continue
        return high_tl

    def get_agility(self):
        """Gets current chassis Agility based on chassis and customizations

        Returns:
            agil: int
        """
        agil = self.agility
        if len(self.chassis_customizations):
            for _ in self.chassis_customizations:
                if _.agility:
                    agil += _.agility
                else:
                    continue
        return agil

    def get_tech_table(self):
        """Gets current chassis Tech Table based on chassis and customizations

        Returns:
            tt: dict
        """
        tt = self.tech_table
        if len(self.chassis_customizations):
            for _ in self.chassis_customizations:
                if _.tech_table:
                    tt = _.tech_table
                    break
        return tt

    def get_traits(self):
        traits = list(self.traits)
        if len(self.chassis_customizations):
            for _ in self.chassis_customizations:
                if _.traits:
                    traits.append(*list(traits))
        return traits

    def get_cost_per_space(self):
        # TODO: this
        """should return correct cost per space for stuff, but maybe a collection of functions to be called for
            different types (see enums.Cost_Types)"""
        pass


class Chassis_Plane(Chassis):
    def __init__(self, name, /, **kwargs):
        # this is maximum possible airstrip, and should be customizable
        self.airstrip: int = kwargs.pop("airstrip", 0)
        super().__init__(name, **kwargs)

    # TODO: do repr


class Chassis_Airship(Chassis):
    def __init__(self, name, /, **kwargs):
        super().__init__(name, **kwargs)
        # this is as a percentage of total spaces in the vehicle
        self.available_spaces: float = 0.1

    # TODO: do repr


class Chassis_Submersible(Chassis):
    def __init__(self, name, /, **kwargs):
        self.sub_table: dict[int: tuple[int, int, int]] = kwargs.pop("sub_table", {})
        super().__init__(name, **kwargs)

    # TODO: do repr


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
        # TODO: add custom armor facing (poss to vehicle obj?)
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')

    # TODO: do repr


class Mount:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        # may be flat, but affected by other factors (e.g. crew, weapons in some cases)
        # [0] = number, [1] = Mount_V_Spaces
        self.vehicle_spaces: tuple[int, int] = kwargs.pop("v_spaces", (0, 0))
        # [0] = spaces, [1] = isResponsive
        self.mount_spaces: tuple[int, int] = kwargs.pop("m_spaces", (0, 0))
        self.base_cost: int = kwargs.pop("cost", 0)
        self.weapon_space_cost: int = kwargs.pop("wep_space_cost", 0)
        # [0] = number, [1] = Mount_Max_Spaces
        self.max_spaces: tuple[int, int] = kwargs.pop("max_spaces", (0, 0))
        self.description: str = kwargs.pop("desc", "N/a")
        self.possible_customizations: tuple[Customization] = kwargs.pop("poss_customizations", ())
        self.possible_weapons: int = kwargs.pop("poss_weapons", 0)
        self.crew_complement: int = kwargs.pop("crew", 0)
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')
        self.customizations: list[Customization] = []
        self.weapons: list[Weapon] = []

    def __repr__(self):
        # TODO: finish repr with all necessary thingums
        return (f"MOUNT OBJECT: {self.name} | V_SPC: {self.vehicle_spaces} | M_SPC: {self.mount_spaces} | "
                f"BASE_COST: {self.base_cost} | W_SPC_COST: {self.weapon_space_cost} | MAX_W_SPC: {self.max_spaces} | "
                f"MOUNT_DESC: {self.description} | CUR_CUSTS: {self.customizations} | CUR_WEAPONS: {self.weapons} | "
                f"CREW_AMT: {self.crew_complement} | POSS_CUSTS: {self.possible_customizations} | "
                f"POSS_WEAPONS: {self.possible_weapons}")


class Mount_Faced(Mount):
    # TODO: do repr
    def __init__(self, name, /, **kwargs):
        self.facing: str = kwargs.pop("facing", "N/a")
        super().__init__(name, **kwargs)


class Customization:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        # [0] = number, [1] = Cost_Type, [2] = is_responsive (increments of 1% Chassis Cost)
        self.cost: tuple[float, int, int] = kwargs.pop("cost", (0, 0, 0))
        # [0] = number, [1] = Space_Type, [2] = is_responsive
        self.spaces: tuple[int, int, int] = kwargs.pop("spaces", (0, 0, 0))
        self.max_spaces: int = kwargs.pop("max_spaces", 0)
        self.this_max_spaces: int = kwargs.pop("this_max_spaces", -1)
        self.this_min_spaces: int = kwargs.pop("this_min_spaces", 0)
        # [0] = number, [1] = speed_type, [2] = not_is_afv
        self.speed: tuple[int, int, int] = kwargs.pop("speed", (0, 0, 0))
        # [0] = number, [1] = range_type
        self.range: tuple[int, int] = kwargs.pop("range", (0, 0))
        # [0] = numer, [1] = shipping_type
        self.shipping: tuple[float, int] = kwargs.pop("shipping", (0.0, 0))
        self.description: str = kwargs.pop("desc", "Lorem ipsum")
        self.traits: tuple[str] = kwargs.pop("traits", ())
        self.tech_table: dict[int: (int, int)] = kwargs.pop("tech_table", {})
        self.skill: str = kwargs.pop("skill", "")
        self.agility: int = kwargs.pop("agility", 0)
        self.tech_level: int = kwargs.pop("tech_level", 1)
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')

    # TODO: do repr


class Customization_Plane(Customization):
    def __init__(self, name, /, **kwargs):
        # this is a multiplier
        self.airstrip: float = kwargs.pop("airstrip", 1.0)
        super().__init__(name, **kwargs)

    # TODO: do repr


class Customization_Airship(Customization):
    def __init__(self, name, /, **kwargs):
        # this is additive
        self.available_spaces: float = kwargs.pop("avail_spaces", 0.0)
        super().__init__(name, **kwargs)

    # TODO: do repr


class Customization_Mount(Customization):
    def __init__(self, name, /, **kwargs):
        self.dice_mod: str = kwargs.pop("dice_mod", "")
        super().__init__(name, **kwargs)

    # TODO: do repr


class Weapon:
    # TODO: make this comply with game rules
    def __init__(self, name, /, **kwargs):
        self.name: str = name
        self.cost: int = kwargs.pop("cost", 0)
        self.spaces: int = kwargs.pop("spaces", 0)
        self.ammo: int = kwargs.pop("ammo", 0)
        self.range: int = kwargs.pop("range", 0)
        self.damage: str = kwargs.pop("damage", "0")
        self.traits: tuple[str] = kwargs.pop("traits", ())
        if kwargs:
            raise TypeError(f'Unsupported configuration options {list[kwargs]}')

    # TODO: do repr

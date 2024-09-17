from .comp_types import Chassis, Armor, Mount, Customization


class Vehicle:

    def __init__(self, name="My New Vehicle", tech_level=1):
        self.name = name
        self.tech_level = tech_level
        self.spaces = 1
        self.chassis: Chassis
        self.armor: Armor
        self.armament = [Mount]
        self.customizations: [Customization]
        self.personnel = {
            "Total Personnel": 0, "Spaces per Person": 0
        }
        # only used for rail riders, default False to prevent users experiencing frustrating behavior
        self.can_off_rail = False

    def get_used_spaces(self):
        """sums all spaces outside the chassis total spaces
        :return used_spaces"""
        pass

    def get_cost(self):
        """needs to be (cost per space * spaces + (sum of everything else))
        :return total_cost"""
        pass

    def get_cargo_space(self):
        """this needs to return (total spaces - used spaces) * 250
        :return cargo_space"""
        pass

    def get_shipping_tonnage(self):
        """this needs to be (total spaces * shipping tonnage per space)"""
        pass

    def get_hull_points(self):
        """this needs to return (hull points per space * spaces)"""
        pass

    def get_spaces(self):
        return self.spaces

    def get_cruise_speed(self):
        """this needs to return 1 speed lower than top speed, unless modified elsewhere"""
        pass

    def get_cruise_range(self):
        """this needs to return 1.5 * range, +/- w/e mods"""
        pass

from .comp_types import Chassis, Armor, Mount, Customization


class Vehicle:

    def __init__(self, name="My New Vehicle", tech_level=1):
        self.name = name
        self.tech_level = tech_level
        self.spaces = 1
        self.chassis: Chassis
        self.armor: Armor
        self.armament: [Mount]
        self.customizations: [Customization]
        self.personnel = {
            "Total Personnel": 0, "Spaces per Person": 0
        }
        # only used for rail riders, default False to prevent users experiencing frustrating behavior
        self.can_off_rail = False

    # TODO: do repr

    def get_used_spaces(self):
        """Sums all Spaces outside the chassis total spaces"""
        pass

    def get_cost(self):
        """Needs to be (cost per space * spaces + (sum of everything else))

            Returns:
                cost: int

        """
        pass

    def get_cargo_space(self):
        """this needs to return (total spaces - used spaces) * 250

            Returns:
                cargo_space: int

        """
        pass

    def get_shipping_tonnage(self):
        """this needs to be (base_spaces * shipping_tonnage_per_space
                                - shipping_tonnage * sum(shipping_tonnage_reduction_pct)
            and, if shipping_tonnage > 30, return max(30, shipping_tonnage/2)

            Returns:
                shipping_tonnage: int

        """
        pass

    def get_hull_points(self):
        """this needs to return (hull points per space * spaces)

            Returns:
                hull_points: int

        """
        pass

    def get_spaces(self):
        return self.spaces

    def get_cruise_speed(self):
        """this needs to return 1 speed lower than top speed, unless modified elsewhere"""
        pass

    def get_cruise_range(self):
        """this needs to return 1.5 * range, +/- w/e mods"""
        pass

    def get_chassis(self):
        """this should return the chassis object"""
        pass

    def get_armaments(self):
        """this should return the list of Mount objects"""
        pass

    def get_customizations(self):
        """this should return the list of Customization objects"""
        pass

    def get_armor(self):
        """this should return the Armor object"""
        pass


"""A set of classes that can be used to represent electric cars"""

from car import Car

class Battery:

    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 200

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65





class Electriccar(Car):
    """represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Init attributes of the parent class."""
        super().__init__(make, model, year)
        """super allows for you to not have to know the parent class's implementation
        if you know the parent class you can replace super with the class e.g. Car.__init__(self, make, model, year)"""
        self.battery = Battery(40)

    #def describe_battery(self):
    #    """Print a statement describing the battery size."""
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("Electric cars don't have gas tanks!")

my_leaf = Electriccar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
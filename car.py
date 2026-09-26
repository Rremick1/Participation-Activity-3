"""a class that can be used to represent a car"""

class Car:
    """a simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill the gas tank."""
        print(f"Filling the gas tank for the {self.get_descriptive_name()}")

#my_new_car = Car('audi', 'a4', 2024)
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#my_new_car.increment_odometer(2)

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

"""
Try it yourself 

9-9 Battery Upgrade

Use the final version of electric_car.py from this section.
add a method to the battery class called 'upgrade_battery()'. This method should check the battery size and set the capacity to 65 if it isn't already.
Make an electric car with a default battery size, call 'get_range()' once, and then call 'get_range()' a second time after upgrading the battery.
You should see an increase in the car's range."""

my_car = Electriccar('tesla', 'model s', 2024)
my_car.battery.battery_size = 40
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
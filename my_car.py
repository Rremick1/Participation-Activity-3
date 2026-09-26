
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.increment_odometer(20)
my_new_car.read_odometer()
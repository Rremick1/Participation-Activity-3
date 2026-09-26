

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog("Rocky", 3)

print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")

my_other_dog = Dog("Jameson", 5)

print(f"my other dog's name is {my_other_dog.name}.")
print(f"my other dog is {my_other_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

my_other_dog.sit()
my_other_dog.roll_over()

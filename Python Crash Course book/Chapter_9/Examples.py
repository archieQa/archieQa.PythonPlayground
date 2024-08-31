class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now siting')

    def roll(self):
        print(f'{self.name} is now rolling')


my_dog = Dog('Nona', 10)
print(f'This is my dog: {my_dog.name} ,{my_dog.age}')
my_dog.sit()
my_dog.roll()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")



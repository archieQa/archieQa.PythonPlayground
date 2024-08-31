# Make a class called Restaurant, two attributes: name and cuisine_type

class Restaurant:
    def __init__(self, name_restaurant, cuisine_type):
        self.name_restaurant = name_restaurant
        self.cuisine_type = cuisine_type
        self.tables_served = 0

    def show_tables_served(self, number):
        self.tables_served = number
        print(number)

    def shtoji_tables_served(self, additional_num):
        self.tables_served += additional_num
        print(self.tables_served)

    def describe_restaurant(self):
        print(f"The Restaurant name is: {self.name_restaurant}")
        print(f"The Restaurant cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f'Restaurant {self.name_restaurant} Is open for customers')


my_rest = Restaurant('Nona', 'Shqiptare')
CJ_rest = Restaurant('CJ', 'Shqiptare')
print(f'Restauranti {CJ_rest.name_restaurant} ka kuzhin {CJ_rest.cuisine_type}')
CJ_rest.describe_restaurant()
CJ_rest.show_tables_served(8)
CJ_rest.shtoji_tables_served(2)


class IceCreamStand(Restaurant):

    def __init__(self, name_restaurant, cuisine_type='Ice Cream'):
        super().__init__(name_restaurant, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print('We have the following flavors: ')
        for flavor in self.flavors:
            print(flavor)


ice_cream = IceCreamStand('Sweat Treats')

ice_cream.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint']
ice_cream.describe_restaurant()
ice_cream.show_flavors()

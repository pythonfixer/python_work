class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant('kfc', 'quick-a')
restaurant.describe_restaurant()

restaurant = Restaurant('mc-donalds', 'quick-b')
restaurant.describe_restaurant()

restaurant = Restaurant('dicos', 'quick-c')
restaurant.describe_restaurant()
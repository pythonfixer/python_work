class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant('kfc', 'quick')

print("Restaurant name: " + restaurant.restaurant_name.title())
print("Restaurant type: " + restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
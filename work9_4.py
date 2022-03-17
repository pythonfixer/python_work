class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type.title())
        
    def open_restaurant(self):
        print("The restaurant is open.")
        
    def set_number_served(self, number):
        self.number_served = number  
        
    def increment_number_served(self, num):
        self.number_served += num
        
restaurant = Restaurant('kfc', 'quick')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

print("There're " + str(restaurant.number_served) + " persons in this restaurant.")
restaurant.number_served = 21
print("There're " + str(restaurant.number_served) + " persons in this restaurant.")
print("\n")

restaurant.set_number_served(27)
print("There're " + str(restaurant.number_served) + " persons in this restaurant.\n")

restaurant.increment_number_served(30)
print("This restaurant can be included " + str(restaurant.number_served) + " persons a day.")


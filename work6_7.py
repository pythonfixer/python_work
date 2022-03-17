people_0 = {
            'first_name': 'jim',
            'last_name': 'green',
            'age': 28,
            'city': 'beijing', 
            }
people_1 = {
            'first_name': 'albert',
            'last_name': 'aeinstein',
            'age': 53,
            'city': 'princeton', 
            }
people_2 = {
            'first_name': 'marie',
            'last_name': 'curie',
            'age': 39,
            'city': 'paris', 
            }
people = [people_0, people_1, people_2]

for peo in people:
    full_name = peo['first_name'] + " " + peo['last_name']
    age = peo['age']
    city = peo['city']
    print("\tFull name: " + full_name.title())
    print("\tAge: " + str(age))
    print("\tCity: " + city.title())



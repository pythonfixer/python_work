tom = {
    'pet_name': 'tom',
    'class': 'cat',
    'owner': 'mike',
    }
jiessie = {
    'pet_name': 'jiessie',
    'class': 'mouse',
    'owner': 'bob',
    }
mickey = {
    'pet_name': 'mickey',
    'class': 'rabbit',
    'owner': 'marry'
        }
pets = [tom, jiessie, mickey]

for pet in pets:
    print("\nPet Name: " + pet['pet_name'].title())
    print("Pet class: " + pet['class'].title())
    print("Owner: " + pet['owner'].title())

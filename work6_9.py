favorite_places = {
    'jack': ['gui lin', 'shang hai', 'nan jing'],
    'mary': ['da lian', 'fu jian', 'hai nan'],
    'bob': ['qing dao', 'xi an', 'bei jing'],
    }

for name, places in favorite_places.items():
    print("I'm " + name.title() + ", my favorite places are:")
    for place in places:
        print(place.title())

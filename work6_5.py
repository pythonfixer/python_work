river_countrys = {'yellow river': 'china', 'nile': 'egypt', 'rhine': 'switzerland'}

for river, country in river_countrys.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in river_countrys.keys():
    print(river.title())

for country in river_countrys.values():
    print(country.title())
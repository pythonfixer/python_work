cities = {
    'xi an': {
        'country': 'china',
        'population': '9056800',
        'fact': 'history famous',
    },
    'paris': {
        'country': 'france',
        'population': '11000000',
        'fact': 'art famous',
    },
    'new york': {
        'country': 'america',
        'population': '8150000',
        'fact': 'economist famous',
    },
}

for city_name, city_infos in cities.items():
    print(city_name.title())
    country = city_infos['country']
    population = city_infos['population']
    fact = city_infos['fact']
    print("\t" + country.title())
    print("\t" + population)
    print("\t" + fact.title())
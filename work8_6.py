def city_countrys(current_city, current_country):
    city_country = {'city': current_city, 'country' : current_country}
    return city_country

city_country = city_countrys('santiago', 'chile')
print(city_country['city'].title() + ", " + city_country['country'].title())

city_country = city_countrys('new york', 'usa')
print(city_country['city'].title() + ", " + city_country['country'].title())

city_country = city_countrys('beijing', 'china')
print(city_country['city'].title() + ", " + city_country['country'].title())

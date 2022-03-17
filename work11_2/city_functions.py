def get_formatted_city(city, country, population=''):
    if population:
        format_city = city + ', ' + country + ' ' + '- population' + ' ' + population
    else:
        format_city = city + ', ' + country
    return format_city.title()

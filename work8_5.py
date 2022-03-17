def describe_city(city, country = 'china'):
    print("\n" + city.title() + " is in " + country.title() + ".")
    
describe_city(city = 'xi an')
describe_city('beijing')

describe_city('reykjavik', 'iceland')

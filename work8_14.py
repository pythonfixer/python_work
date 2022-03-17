def make_car(maker, serial, **car_info):
    profile = {}
    profile['maker_name'] = maker
    profile['serial_name'] = serial
    for key, value in car_info.items():
        profile[key] = value
    return profile
    
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

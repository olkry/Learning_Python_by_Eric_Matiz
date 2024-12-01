def car_information_constructor(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

my_car = car_information_constructor('Toyota', 'Corolla', color='Red', complete_set=True)

print(my_car)
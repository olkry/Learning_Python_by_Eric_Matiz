def name_city_builder(city, country):
    full_name = f'{city}, {country}'
    return full_name.title()


city_1 = name_city_builder('Moscow', 'Russia')
print(city_1)
city_2 = name_city_builder('berlin', 'germany')
print(city_2)
city_3 = name_city_builder(country='Great britain', city='london')
print(city_3)
rivers = {'Лена': "Россия", "рейн": "Германия", "темза": "Англия", "ефрат": "месопотамия"}

for key, values in rivers.items():
    print(f'Река {key.title()} располагается в {values.title()}')

for name in rivers.keys():
    print(name.title())

for country in rivers.values():
    print(country.title())
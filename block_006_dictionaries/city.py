cities = {
    'moscow': {
        'country': 'Russia',
        'population': 15000000,
        'fact': 'Capital of Russia'
    },
    'barcelona': {
        'country': 'Spain',
        'population': 6000000,
        'fact': 'Most beautiful town in Spain'
    },
    'kiyoto': {
        'country': 'Japan',
        'population': 9000000,
        'fact': 'A city that supports traditional culture'
    },
}

for city, values in cities.items():
    print(f'Город: {city.title()}')
    print(f'Страна: {values['country']}')
    print(f'Население города примерно {values['population']}')
    print(f'{values['fact']}\n')
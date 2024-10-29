

human = {
    'first_name': "Gasty",
    'last_name': 'Mareno',
    'city': 'Moscow'
}
human_2 = {
    'first_name': "Salvador",
    'last_name': 'Dali',
    'city': 'Barcelona'
}
human_3 = {
    'first_name': "Herman",
    'last_name': 'Hesse',
    'city': 'Berlin'
}
people = [human, human_2, human_3]

# print(human['first_name'])
# print(human['last_name'])
# print(human.get('city', 'City is not available'))

for person in people:
    print(f'Name: {person['first_name']} {person['last_name']}')
    print(f'Hometown: {person['city']}\n')
friends = {
    'Herman': [108, 69],
    'Cloud': [1, 7],
    'Sephiroth': [42, 16, 38],
    "Gabriel": [192],
    "Alucard": [667, 665]
    }

# favorite_numbers = (f'Herman - {friends['Herman']} \nCloud - {friends['Cloud']} '
#                     f'\nSephiroth - {friends['Sephiroth']} \nGabriel - {friends["Gabriel"]} '
#                     f'\nAlucard - {friends["Alucard"]}')
#
# print(favorite_numbers)

for name, numbers in friends.items():
    print(f'\nУ {name.title()} любимые числа:')
    for numb in numbers:
        print(f'-\t{numb}')
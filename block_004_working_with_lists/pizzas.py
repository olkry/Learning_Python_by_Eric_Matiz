pizzas = ['4 сыра', "Бургерная", "Диабло"]

# for pizza in pizzas:
#     print(f'Я люблю пиццу - {pizza}')
# print('\nЯ очень люблю пиццу')

friend_pizzas = pizzas[:]
pizzas.append('Пепперони')
friend_pizzas.append('Гавайская')

print('My favorite pizzas:')
for piz in pizzas:
    print(f'\t{piz}')

print('\nMy friend favorite pizzas:')
for piz in friend_pizzas:
    print(f'\t{piz}')



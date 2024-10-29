veda = {
    'name': 'Oleg',
    'class': 'cat'
}
charly = {
    'name': 'Igor',
    'class': 'dog'
}
ketya = {
    'name': 'Liza',
    'class': 'cat'
}

pets = [veda, charly, ketya]

for pet in pets:

    print(f'Имя владельца: {pet["name"]}')
    print(f'Вид животного: {pet["class"]}')

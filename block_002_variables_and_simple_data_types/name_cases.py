name = "Олег"

print(f'Hello {name} nice to meet you.')

first_name = 'Олег'
last_name = "крючихин"
full_name = f'{first_name} {last_name}'
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

quote = 'Стремитесь не к успеху, а к ценностям, которые он дает'
autor = 'Альберт Эйнштейн'
print(f'{autor} однажды сказал: "{quote}"')

message = f'{autor} однажды сказал: "{quote}"'
print(message)

test_inscrypt = '\tКрючихин\n\tОлег\n\tИгоревич\t  '
test_inscrypt = '   \nКрючихин Олег Игоревич\t  '
print(test_inscrypt)
print(test_inscrypt.rstrip())
print(test_inscrypt.lstrip())
print(test_inscrypt.strip())


names_login = ['Herman', "Alexandra", 'Admin', 'Fofnatiy', "Mareno"]
current_user = ['Herman', "Alexandra", 'Admin', 'Fofnatiy', "Mareno"]
new_user = ['Jess', "Alexandra", 'Silvana', 'Rudy', "MARENO"]

if names_login:
    for name in names_login:
        if name.lower() == 'admin':
            print(f'С возвращением, администратор, желаете просмотреть последние логи?')
        else:
            print(f'Приветствую, {name}, приятно вас видеть, снова.')
    print('\n__Регистрация новых пользователей__\n')
    for new in new_user:
        if new.title() not in current_user:
            print(f'Приветствую, {new}, вы успешно зарегистрировались!')
        else:
            print(f'Имя {new} уже занято')
else:
    print("Список пуст.")


import json


def get_new_username():
    filename = 'text_files/username.json'
    username = input(f'Вы у нас первый раз, как Вас зовут?\n>')
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def get_stored_username():
    filename = 'text_files/username.json'
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def greet_user(name):
    """Приветствует пользователя по имени"""
    if name:
        print(f'С возвращением, {name}!')

    else:
        username = get_new_username()
        print(f'Я Вас запомнил, {username}.')


def user_check():
    login = input('Login: ').lower()
    name = get_stored_username()
    if name and name.lower() == login:
        greet_user(name)
    else:
        new_name = get_new_username()
        print(f'Добро пожаловать, {new_name}')


if __name__ == '__main__':
    user_check()
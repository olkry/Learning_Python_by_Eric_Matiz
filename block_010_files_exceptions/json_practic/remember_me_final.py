import json




# filename = 'file_hub/username.json'
#
# try:
#     with open(filename) as f:
#         name = json.load(f)
#
# except FileNotFoundError:
#     username = input(f'Вы у нас первый раз, как Вас зовут?\n>')
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f'Я Вас запомнил, {username}.')
# else:
#     print(f'С возвращением, {name}!')

### Рефакторинг

def get_new_username():
    filename = 'file_hub/username.json'
    username = input(f'Вы у нас первый раз, как Вас зовут?\n>')
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def get_stored_username():
    filename = 'file_hub/username.json'
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def greet_user():
    """Приветствует пользователя по имени"""
    name = get_stored_username()
    if name:
        print(f'С возвращением, {name}!')

    else:
        username = get_new_username()
        print(f'Я Вас запомнил, {username}.')


if __name__ == '__main__':
    greet_user()

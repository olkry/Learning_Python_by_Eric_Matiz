import json

filename = 'text_files/favorite_number.json'


def get_number(path):
    '''
    Загрузить данные с файла
    :param path: путь до файла
    :return:
    '''
    try:
        with open(path) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def remember_number(path):
    user_number = input(f'Введите Ваше любимое число: ')
    with open(path, 'w') as f:
        json.dump(user_number, f)


def show_number(path):
    number = get_number(path)
    if number:
        print(f'Ваше любимое число - {number}')
    else:
        remember_number(path)
        print(f'Я запомнил Ваше число.')


if __name__ == '__main__':
    show_number(filename)

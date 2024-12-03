from random import choice

gen_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
win_code = ''


def generate(chars, length):
    """
    Генератор комбинации из переданных чисел
    :param chars: Список символов
    :param length: длина комбинации
    :return: Сгенерированная комбинация
    """
    gen_result = ''
    for _ in range(length):
        gen_result += str(choice(chars))
    return gen_result

# print(f'Выигрышная комбинация: {win_code}')

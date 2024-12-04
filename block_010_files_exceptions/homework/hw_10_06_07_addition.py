

print('Введите два числа, я их сложу.')
print("Введите 'q' для выхода.")

while True:
    first_num = input('\nВведите первое число: ')
    if first_num == 'q':
        break
    second_num = input('Введите второе число: ')
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print('Необходимо ввести два числа для сложения или "q" для выхода.')
    else:
        print(answer)
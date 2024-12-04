file_path = 'C:\\Learning_Python_by_Eric_Matiz\\block_010_files_exceptions\\text_files\\pi_million_digits.txt'

# сохранить числа из пи до ляма.
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# # напичатать первые 52 числа из пи до ляма.
# print(f'{pi_string[:52]}...')
# print(len(pi_string))

# Проверить есть ли ДР в пи до ляма
birthday = input("Введите дату Вашего ДР в формате ддммгг: ")
if birthday in pi_string:
    print('Да, есть!')
else:
    print("Увы, нет(")


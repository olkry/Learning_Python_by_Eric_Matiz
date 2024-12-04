file_path = 'C:\\Learning_Python_by_Eric_Matiz\\block_010_files_exceptions\\text_files\\pi_digits.txt'
# Полное чтение файла
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# Построчное чтение файла
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Построчная запись в переменную
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
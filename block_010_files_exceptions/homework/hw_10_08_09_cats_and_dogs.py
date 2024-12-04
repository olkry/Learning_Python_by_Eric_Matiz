# with open('text_files/cat.txt', 'w', encoding='utf-8') as f:
#     f.write('Веда\nМаша\nАся')
#
# with open('text_files/dog.txt', 'w', encoding='utf-8') as f:
#     f.write('Чарли\nУма\nДик')


def name_reader(folder, file, extension):
    filename = folder + file + extension
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
        # print(f'\nФайла {file} нет в папке {folder}')
    else:
        print(f'\nФайл {file} содержит следующую информацию:')
        print(content.strip())


folder = 'text_files/'
files = ['cat', 'dog']
extension = '.txt'

for file in files:
    name_reader(folder, file, extension)
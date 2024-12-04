folder = 'C:\\Learning_Python_by_Eric_Matiz\\block_010_files_exceptions\\text_files\\'
files = ['alice', 'little_women', 'moby_dick']
ref = '.txt'

def word_counter(filepath, word, file):
    try:
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Файла {file} нет в хранилище')
    else:
        counter = content.lower().count(word)
        print(f'В книге {file} слово {word} встречается {counter} раз')


word = input('Какое слово желаете найти: ')
for file in files:
    filename = folder+file+ref
    word_counter(filename, word, file)
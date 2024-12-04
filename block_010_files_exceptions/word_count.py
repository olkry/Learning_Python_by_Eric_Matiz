def word_count(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f'Sorry, file {filename} dos not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has {num_words} words.')


folder = 'text_files/'
filename = 'text_files/alice.txt'
filenames = [folder + 'alice.txt', folder + 'siddhartha.txt', folder + 'moby_dick.txt', folder + 'little_women.txt']

for file in filenames:
    word_count(file)

filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry, file {filename} dos not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has {num_words} words.')
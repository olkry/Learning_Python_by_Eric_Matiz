file_name = 'text_files/guests_book.txt'

with open(file_name, 'w') as file:
    while True:
        name = input('Inter yore name if close enter "q": ')
        if name == 'q':
            break
        else:
            file.write(f'{name} has join!\n')
            print(f'Welcome, {name}')



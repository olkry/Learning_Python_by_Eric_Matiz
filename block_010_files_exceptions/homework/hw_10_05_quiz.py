file_name = 'text_files/quiz.txt'

with open(file_name, 'w') as file:

    while True:
        answer = input('Write your reason for join to Python or "q" to exit: ')
        if answer != 'q':
            file.write(f'Reason for join to Python: {answer}\n')
            print('Thanks for your answer!\n')
        else:
            print('By!')
            break
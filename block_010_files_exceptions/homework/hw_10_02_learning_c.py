file_name = 'text_files/learning_python.txt'

with open(file_name, encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    print(line.replace('Пайтон', "С").strip())
    # print(repa.strip())
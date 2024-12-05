import json

filename = 'file_hub/username.json'
username = input('Привет, как тебя зовут?\n>')

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f'Я запомню тебя, {username}, буду ждать!')

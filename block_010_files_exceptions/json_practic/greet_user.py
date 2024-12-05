import json

filename = 'file_hub/username.json'

with open(filename) as f:
    name = json.load(f)
    print(f'С возвращением, {name}!')
    
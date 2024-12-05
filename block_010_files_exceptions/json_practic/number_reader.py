import json

filename = 'file_hub/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

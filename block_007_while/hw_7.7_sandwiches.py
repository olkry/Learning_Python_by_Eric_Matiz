sandwich_menu = ["томатный", "тунцовый", "постный", "карбонара", "говяжий"]
ready_made_sandwiches = []

while sandwich_menu:
    sandwich = sandwich_menu.pop()
    print(f"Начинаем приготовление: {sandwich} сендвич")
    ready_made_sandwiches.append(sandwich)

print("\nГотовые сендвичи:")
for sandwich in ready_made_sandwiches[::-1]:
    print(f'\t{sandwich} сендвич')




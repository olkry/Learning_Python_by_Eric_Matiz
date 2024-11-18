sandwich_menu = ["томатный", "пастарами", "тунцовый", "постный", "пастарами", "карбонара", "говяжий", "пастарами"]
ready_made_sandwiches = []

print("Извиняемся за неудобства, сендвичи пастарами закончились((\n")

while sandwich_menu:
    sandwich = sandwich_menu.pop()
    if sandwich == "пастарами":
        continue
    else:
        print(f"Начинаем приготовление: {sandwich} сендвич")
        ready_made_sandwiches.append(sandwich)

print("\nГотовые сендвичи:")
for sandwich in ready_made_sandwiches[::-1]:
    print(f'\t{sandwich} сендвич')


    dream_vacation


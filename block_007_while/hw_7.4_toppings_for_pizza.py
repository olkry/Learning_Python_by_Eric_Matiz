toppings = []
message = '\nКакой топпинг желаете добавить?\nЕсли желаете выйти нажмите q\n>>> '

while True:
    topping = input(message)

    if topping == 'q':
        break

    else:
        toppings.append(topping)
        print(f'Вы добавили {topping}')


print("\nВы выбрали пиццу со следующими топпингами:")
for top in toppings:
    print(f'\t{top}')




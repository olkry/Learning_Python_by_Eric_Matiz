def sandwich_maker(*toppings):
    print('Ваш сэндвич будет сделан из:')
    for topping in toppings:
        print(f'> {topping}')
    print('Приступаем к готовке\n')

ingredients = ['буженина', 'бекон']

sandwich_maker('томат')
sandwich_maker('пасиарами', 'огурец', 'помидор')
sandwich_maker(*ingredients)
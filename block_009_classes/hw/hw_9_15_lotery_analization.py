from block_009_classes.hw.hw_9_14_lotery import generate, gen_numbers

win_combination = generate(gen_numbers, 6)

def how_meny_ticket(my_com, win):
    number_tickets = 1
    while my_com != win:
        number_tickets += 1
        win = generate(gen_numbers, 6)
    return number_tickets

if __name__ == '__main__':
    my_combination = '235658'
    need_tickets = how_meny_ticket(my_combination, win_combination)
    print(f'Вы выиграли, комбинация {my_combination} выпала... с {need_tickets} билета')
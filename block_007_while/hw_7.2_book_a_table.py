
number_of_seats = int(input("На сколько мест Вы бронируете стол?\n>>> "))

if number_of_seats > 8:
    print(f'Идет поиск стола на {number_of_seats} мест. Это может занять некоторое время.')
else:
    print("Стол успешно забронирован!")


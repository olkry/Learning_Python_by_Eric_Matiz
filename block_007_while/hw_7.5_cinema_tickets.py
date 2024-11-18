number_of_tickets = int(input("Количество билетов: "))
age_request = "На какой возраст приобретаете билет?\n>>> "
price = 0

while number_of_tickets:
    age = int(input(age_request))

    if age < 3:
        price += 0
        print("Цена билета 0$\n")
        number_of_tickets -= 1

    elif age < 12:
        price += 10
        print("Цена билета 10$\n")
        number_of_tickets -= 1

    else:
        price += 15
        print("Цена билета 15$\n")
        number_of_tickets -= 1

print(f"\nОбщая стоимость: {price}$")


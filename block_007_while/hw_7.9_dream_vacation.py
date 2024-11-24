vacations = {}
message = 'Желаете добавить человека в список отпусков, выход из программы "q"\n'
name_request = "Введите Ваше имя: "
location_request = "Где вы мечтаете отдохнуть?\n>>>"

while True:
    controller = input(message)

    if controller == "q":
        break
    else:
        name = input(name_request)
        loc = input(location_request)
        vacations[name] = loc
        print(f"{name}, успешно добавили вашу желаемую точку маршрута - {loc}\n")

print("\nНа данный момент мы имеем следующие данные:")

for keys in vacations:
    print(f'{keys.title()} желает посетить {vacations[keys].title()}')
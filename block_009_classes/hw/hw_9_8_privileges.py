class Privileges:

    def __init__(self, *privileges):
        self.privileges = ("Добавление", "Удаление", "Бан", "Редактирование") + privileges

    def show_privileges(self):
        print("\nВам доступны следующие действия: ")
        for moves in self.privileges:
            print(F'> {moves}')

    def add_duties(self, *duties):
        self.privileges += duties
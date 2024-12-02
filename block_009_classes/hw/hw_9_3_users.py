class User:

    def __init__(self, first_name, last_name, age, type_user):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.access = type_user

    def describe_user(self):
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Пользователю {full_name.title()} {self.age} лет, доступ - {self.access}.')

    def greet_user(self):
        print(f'{self.first_name} рады Вас видеть!')


if __name__ == '__main__':

    user_1 = User("Вася", "Начальников", 46, "менеджер")
    user_2 = User("Тося", "Умарова", 28, "администратор")

    user_1.describe_user()
    user_2.describe_user()

    user_1.greet_user()
    user_2.greet_user()
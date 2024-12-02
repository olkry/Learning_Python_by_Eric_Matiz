class User:

    def __init__(self, first_name, last_name, age, type_user='user'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.access = type_user
        self.login_attempts = 0

    def describe_user(self):
        full_name = f'{self.first_name} {self.last_name}'
        print(f'\nПользователь {full_name.title()} {self.age} лет, доступ - {self.access}.')

    def greet_user(self):
        print(f'{self.first_name} рады Вас видеть!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':

    user_1 = User('Vasia', 'Pupkin', 25)
    user_1.describe_user()
    user_1.increment_login_attempts()
    user_1.increment_login_attempts()
    print(user_1.login_attempts)
    user_1.reset_login_attempts()
    print(user_1.login_attempts)

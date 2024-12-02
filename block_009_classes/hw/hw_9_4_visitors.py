class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Информация о ресторане"""
        print(f'В ресторане "{self.name}" представлена {self.type} кухня.')

    def open_restaurant(self):
        print(f'В настоящее время ресторан "{self.name}" открыт.')

    def served_client(self):
        print(f'Обслужено {self.number_served} человек')

    def set_number_served(self, client):
        if client >= self.number_served:
            self.number_served = client
        else:
            print('Вы уже обслужили большее число, используйте другой метод!')

    def increment_number_served(self, client):
        self.number_served += client




if __name__ == '__main__':

    rest_1 = Restaurant("Ля Журнён", "французская")
    rest_1.served_client()
    rest_1.number_served = 26
    rest_1.served_client()
    rest_1.set_number_served(49)
    rest_1.served_client()
    rest_1.increment_number_served(50)
    rest_1.served_client()

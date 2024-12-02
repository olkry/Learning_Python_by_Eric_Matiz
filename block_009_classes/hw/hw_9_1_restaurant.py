class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Информация о ресторане"""
        print(f'В ресторане "{self.name}" представлена {self.type} кухня.')

    def open_restaurant(self):
        print(f'В настоящее время ресторан "{self.name}" открыт.')


my_restaurant = Restaurant("Пиццатакия", "итальянская и греческая")


if __name__ == '__main__':

    print(my_restaurant.name)
    print(my_restaurant.type)
    my_restaurant.open_restaurant()
    my_restaurant.describe_restaurant()
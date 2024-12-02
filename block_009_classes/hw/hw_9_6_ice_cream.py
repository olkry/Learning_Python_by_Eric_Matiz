from hw_9_4_visitors import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *sorts):
        super().__init__(restaurant_name, cuisine_type)
        self.sorts = sorts

    def all_sorts(self):
        print("\nДоступные сегодня сорта:")
        for sort in self.sorts:
            print(f'> {sort}')

if __name__ == '__main__':

    store_1 = IceCreamStand("МаксиКолд", "заморозка", "эскимо", "пломбир", "крем-брюле")
    store_1.describe_restaurant()
    store_1.all_sorts()
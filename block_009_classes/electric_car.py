from block_009_classes.car import Car
from block_009_classes.battery import Battery

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()





if __name__ == '__main__':

    my_elec_car_1 = ElectricCar('tesla', 'model s', 2019)
    print(my_elec_car_1.get_descriptive_name())
    my_elec_car_1.battery.describe_battery()
    my_elec_car_1.battery.get_range()
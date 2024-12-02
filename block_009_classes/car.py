class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def odometer_update(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles




if __name__ == '__main__':

    my_car = Car('audi', 'a4', 2019)
    print(my_car.get_descriptive_name())

    my_car.odometer_update(1800)
    my_car.read_odometer()

    my_car.increment_odometer(700)
    my_car.read_odometer()

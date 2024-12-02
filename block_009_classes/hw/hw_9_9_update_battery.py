from block_009_classes.electric_car import ElectricCar


my_car = ElectricCar('Toyota', 'Corolla', 2007)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()


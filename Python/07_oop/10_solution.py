# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is Battery Info."

class Engine:
    def engine_info(self):
        return "This is Engine Info."

class ElctricCar(Battery,Engine):
    pass

my_car = ElctricCar()
print(my_car.battery_info())
print(my_car.engine_info())

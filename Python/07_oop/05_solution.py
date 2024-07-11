# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):   #1
        return "Petrol and Diesel"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):   #2
        return "Electric charge"



my_tesla = ElectricCar("Tesla","Model S","85kWh")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())  #2

safari = Car("Tata","Safari")
print(safari.fuel_type())   #1
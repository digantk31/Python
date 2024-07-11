# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    @staticmethod
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or an electric motor."

    @staticmethod
    def is_motor_vehicle(vehicle_type):
        motor_vehicles = ["car", "motorcycle", "truck", "bus"]
        return vehicle_type.lower() in motor_vehicles

# Example usage
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_description())            # Output: 2020 Toyota Corolla
print(Car.general_description())           # Output: A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or an electric motor.
print(my_car.general_description())        # Output: A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or an electric motor.

print(Car.is_motor_vehicle("car"))         # Output: True
print(my_car.is_motor_vehicle("bicycle"))  # Output: False

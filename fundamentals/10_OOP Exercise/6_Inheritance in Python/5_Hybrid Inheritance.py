'''
When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.
'''

class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Truck class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()

'''
Note: In the above example, hierarchical and multiple inheritance exists. 
Here we created, parent class Vehicle and two child classes named Car and Truck this is hierarchical inheritance.
Another is SportsCar inherit from two parent classes named Car and Vehicle. 
This is multiple inheritance.
'''
        
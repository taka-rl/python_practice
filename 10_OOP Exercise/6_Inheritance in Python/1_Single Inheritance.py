'''
In single inheritance, a child class inherits from a single-parent class. 
Here is one child class and one parent class.
'''

# Base class
class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")

# Child class
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

# Create object of Car
car = Car()

# acess Vehicle's info using car object
car.Vehicle_info()
car.car_info()

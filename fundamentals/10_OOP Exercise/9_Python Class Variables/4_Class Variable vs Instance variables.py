'''
Instance variables: Instance variable’s value varies from object to object. 
Instance variables are not shared by objects. Every object has its own copy of the instance attribute

Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method. 
Class variables are shared by all instances of a class.

'''

class Car:
    # Class variable
    manufacture = "BME"
    
    def __init__(self, model, price):
        # instance variable
        self.model = model
        self.price = price

# create object
car = Car("x1", 2500)
print(car.model, car.price, Car.manufacture)

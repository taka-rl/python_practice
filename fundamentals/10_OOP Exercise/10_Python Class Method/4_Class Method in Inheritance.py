'''
In inheritance, the class method of a parent class is available to a child class.
Let’s create a Vehicle class that contains a factory class method from_price() that will return a Vehicle instance from a price. 
When we call the same method using the child’s class name, it will return the child’s class object.
Whenever we derive a class from a parent class that has a class method then it creates the correct instance of the derived class. 
The following example shows how the class method works in inheritance.

'''
class Vehicle:
    brand_name = "BMW"
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 76
        # create new Vehicle object
        return cls(name, (price * 75))
    
    def show(self):
        print(self.name, self.price)
        
class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, "Mileage", mileage)

bmw_us = Car("BMW X5", 65000)
bmw_us.show()

# class method of parent class is available to child class
# this will return the object of calling class
bmw_ind = Car.from_price("BMW X5", 65000)
bmw_ind.show()

# check type
print(type(bmw_ind))


'''
In inheritance, all members available in the parent class are by default available in the child class. 
If the child class does not satisfy with parent class implementation, 
then the child class is allowed to redefine that method by extending additional functions in the child class. 
This concept is called method overriding.
When a child class method has the same name, same parameters, and same return type as a method in its superclass, 
then the method in the child is said to override the method in the parent class.
'''

class Vehicle:
    def max_speed(self):
        print("max speed is 100 km/Hour")

class Car(Vehicle):
    # pverridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()

'''
In the above example, we create two classes named Vehicle (Parent class) and Car (Child class).
The class Car extends from the class Vehicle so, all properties of the parent class are available in the child class. 
In addition to that, the child class redefined the method max_speed().

'''


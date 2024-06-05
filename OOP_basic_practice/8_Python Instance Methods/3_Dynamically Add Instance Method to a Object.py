'''
Usually, we add methods to a class body when defining a class. 
However, Python is a dynamic language that allows us to add or delete instance methods at runtime. 
Therefore, it is helpful in the following scenarios.

When class is in a different file, and you don’t have access to modify the class structure
You wanted to extend the class functionality without changing its basic structure because many systems use the same structure.

'''

import types

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method:
    def show(self):
        print("Name:", self.name, "Age:", self.age)
    
# create new method
def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")

# create object
s1 = Student("Jessa", 15)

# Add instance method to object
s1.welcome = types.MethodType(welcome, s1)
s1.show()

# call newly added method
s1.welcome()

'''
object.XXX = types.MethodType(XXX, object)
→an instance method "XXX" can be added to an object "object" 

'''
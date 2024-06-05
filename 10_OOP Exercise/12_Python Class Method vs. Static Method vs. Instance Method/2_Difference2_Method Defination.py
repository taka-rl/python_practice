'''
Difference #2: Method Defination
Let’s learn how to define instance method, class method, and static method in a class. 
All three methods are defined in different ways.

All three methods are defined inside a class, and it is pretty similar to defining a regular function.
Any method we create in a class will automatically be created as an instance method. 
We must explicitly tell Python that it is a class method or static method.
Use the @classmethod decorator or the classmethod() function to define the class method
Use the @staticmethod decorator or the staticmethod() function to define a static method.
Example:

Use self as the first parameter in the instance method when defining it. 
The self parameter refers to the current object.
On the other hand, Use cls as the first parameter in the class method when defining it.
The cls refers to the class.
A static method doesn’t take instance or class as a parameter because they don’t have access to the instance variables and class variables.

'''

class Student:
    # class variables
    school_name = "ABC School"
    
    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
    
    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)
    
    @classmethod
    def change_school(cls, name):
        cls.school_name = name
    
    @staticmethod
    def find_notes(subject_name):
        return ["chapter1", "chapter2", "chapter3"]


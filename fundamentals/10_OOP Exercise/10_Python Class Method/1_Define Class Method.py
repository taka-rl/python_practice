'''
In method implementation, if we use only class variables, we should declare such methods as class methods. 
The class method has a cls as the first parameter, which refers to the class.
Class methods are used when we are dealing with factory methods. 
Factory methods are those methods that return a class object for different use cases. 
Thus, factory methods create concrete implementations of a common interface.
'''

# Example 1: Create Class Method Using @classmethod Decorator

from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age and set it as an age
        # return new object
        return cls(name, date.today().year - birth_year)
    
    def show(self):
        print(self.name + "'s age is:" + str(self.age))

jessa = Student("Jessa", 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()

'''
In the above example, we created two objects, one using the constructor and the second using the calculate_age() method.
The constructor takes two arguments name and age. On the other hand, class method takes cls, name, and birth_year and returns a class instance which nothing but a new object.
The @classmethod decorator is used for converting calculate_age() method to a class method.
The calculate_age() method takes Student class (cls) as a first parameter and returns constructor by calling Student(name, date.today().year - birthYear), which is equivalent to Student(name, age).

'''
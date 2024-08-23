'''
We can access static variables either by class name or by object reference, but it is recommended to use the class name.

In Python, we can access the class variable in the following places
Access inside the constructor by using either self parameter or class name.
Access class variable inside instance method by using either self of class name
Access from outside of class by using either object reference or class name.
'''

## Example 1: Access Class Variable in the constructor

class Student:
    # Class variable
    school_name = "ABC School"
    
    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)

# create object

# create first object
s1 = Student("Emma")


## Example 2: Access Class Variable in Instance method and outside class
class Student:
    # Class variable
    school_name = "ABC School"
    
    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        
    # Instance method
    def show(self):
        print("Inside instance method")
        # access using self
        print(self.name, self.roll_no, self.school_name)
        # access using class name
        print(Student.school_name)

# create object
s1 = Student("Emma", 10)
s1.show()

print("Outside class")
# access class variable outside class
# access using object reference
print(s1.school_name)

# access using class name
print(Student.school_name)
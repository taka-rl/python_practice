'''
A class variable is declared inside of class, but outside of any instance method or __init__() method.

By convention, typically it is placed right below the class header and before the constructor method and other methods.
'''

class Student:
    # Class variable
    school_name = "ABC School"
    
    def __init__(self, name , roll_no):
        self.name = name
        self.roll_no = roll_no

# create first object
s1 = Student("Emma", 10)
# access class variable
print(s1.name, s1.roll_no, Student.school_name)

# create second object
s2 = Student("Jessa", 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)

'''
In the above example, we created the class variable school_name and accessed it using the object and class name.

Note: Like regular variables, class variables can store data of any type. 
We can use Python list, Python tuple, and Python dictionary as a class variable.
'''

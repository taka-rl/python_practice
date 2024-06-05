class Student:
    # Class variable
    school_name = "ABC School"
    
    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name)

# create object
s1 = Student("Emma", 10)
print("Before")
s1.show()

# Modify class variable
Student.school_name = "XYZ School"
print("After")
s1.show()


'''
Note:

It is best practice to use a class name to change the value of a class variable. 
Because if we try to change the class variable’s value by using an object, a new instance variable is created for that particular object, which shadows the class variables.

'''

# Example:
class Student:
    # Class variable
    school_name = "ABC School"
    
    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create object
s1 = Student("Emma", 10)
s2 = Student("Jessa", 20)

print("Before")
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# modify class variable using object reference
s1.school_name = "PQR School"
print("After")
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

'''
A new instance variable is created for the s1 object, and this variable shadows the class variables.
So always use the class name to modify the class variable.
'''
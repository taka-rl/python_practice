'''
In Python, we use the del statement and delattr() function to delete the attribute of an object. 
Both of them do the same thing.

del statement: The del keyword is used to delete objects. 
In Python, everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list, etc.
delattr() function: Used to delete an instance variable dynamically.

Note: When we try to access the deleted attribute, it raises an attribute error.

'''

## Example 1: Using the del statement
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

# create object
s1 = Student(10, "Jessa")
print(s1.roll_no, s1.name)

# del name
del s1.name

# Try to access name variable
print(s1.name)


## Example 2:delattr() function
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

    def show(self):
        print(self.roll_no, self.name)

s1 = Student(10, 'Jessa')
s1.show()

# delete instance variable using delattr()
delattr(s1, 'roll_no')
s1.show()

'''
We can add instance variables from the outside of class to a particular object. 
Use the following syntax to add the new instance variable to the object.

object_referance.variable_name = value

'''

class Student:
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print("Before")
print("Name:", stud.name, "Age:", stud.age)

# add new instance variable "marks" to stud
stud.marks = 75
print("After")
print("Name:", stud.name, "Age:", stud.age, "Marks:", stud.marks)


'''
Note:
We cannot add an instance variable to a class from outside because instance variables belong to objects.
Adding an instance variable to one object will not be reflected the remaining objects because every object has a separate copy of the instance variable.
'''
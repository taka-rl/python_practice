'''
Using the class method, we can only access or modify the class variables. 
Let’s see how to access and modify the class variables in the class method.
Class variables are shared by all instances of a class. 
Using the class method we can modify the class state by changing the value of a class variable that would apply across all the class objects.
'''

# Example 3: Access Class Variables in Class Methods

class Student:
    school_name = "ABC School"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name
    
    # instance method
    def show(self):
        print(self.name, self.age, "School:", Student.school_name)

jessa = Student("Jessa", 20)
jessa.show()

# change school_name
Student.change_school("XYZ School")
jessa.show()
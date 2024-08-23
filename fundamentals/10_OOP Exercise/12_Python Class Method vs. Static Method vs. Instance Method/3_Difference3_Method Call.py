'''
Difference #3: Method Call
Class methods and static methods can be called using ClassName or by using a class object.
The Instance method can be called only using the object of the class.

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
        print("school name changed to", cls.school_name)
    
    @staticmethod
    def find_notes(subject_name):
        return ["chapter1", "chapter2", "chapter3"]

# create object
jessa = Student("Jessa", 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_school("XYZ School")

# call class method using the object
jessa.change_school("PQR School")

# call static method using the class
Student.find_notes("Math")

# call class method using the object
jessa.find_notes("Math")

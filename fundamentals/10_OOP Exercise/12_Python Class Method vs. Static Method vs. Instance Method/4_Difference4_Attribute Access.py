'''
Both class and object have attributes. 
Class attributes include class variables, and object attributes include instance variables.

・The instance method can access both class level and object attributes. 
Therefore, It can modify the object state.

・Class methods can only access class level attributes. 
Therefore, It can modify the class state.

・A static method doesn’t have access to the class attribute and instance attributes. 
Therefore, it cannot modify the class or object state.
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
        # access instance variables
        print("Student:", self.name, self.age)
        # access class variables
        print("School:", self.school_name)
    
    @classmethod
    def change_school(cls, name):
        #access class variable
        print("Previous school name:", cls.school_name)
        cls.school_name = name
        print("school name changed to", Student.school_name)
    
    @staticmethod
    def find_notes(subject_name):
        # can't access instance or class attributes
        return ["chapter1", "chapter2", "chapter3"]

# create object
jessa = Student("Jessa", 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_school("XYZ School")


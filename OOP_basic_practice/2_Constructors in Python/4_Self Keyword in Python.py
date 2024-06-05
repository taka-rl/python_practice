## Self Keyword in Python

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # self points to the current object
    def show(self):
        # access instance variable using self
        print(self.name, self.age)
        
# creating first object
emma = Student('Emma', 12)
emma.show()

kelly = Student('Kelly', 13)
kelly.show()
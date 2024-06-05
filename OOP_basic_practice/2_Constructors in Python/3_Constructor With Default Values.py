## Constructor With Default Values
class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age = 12, classroom = 7):
        self.name = name
        self.age = age
        self.classroom = classroom
    
    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)
        
# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()
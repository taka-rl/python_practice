class Course:
    # class variable
    course = "Python"
    print("1")

class Student(Course):
    def __init__(self, name):
        self.name = name
        print("2")
    
    def show_student(self):
        # Accessing class variable of parent class
        print("Before")
        print("Student name:", self.name, "Course Name:", Student.course)
        
        # changing class variable value of base class
        print("Now")
        Student.course = "Machine learnig"
        print("Student name:", self.name, "Course Name:", Student.course)
        
        print("3")

# creating object of Student class
stud = Student("Emma")
stud.show_student()



###################################

'''
What if both child class and parent class has the same class variable name.
In this case, the child class will not inherit the class variable of a base class. 
So it is recommended to create a separate class variable for child class instead of inheriting the base class variable.

'''
# Example:

class Course:
    # class variable
    course = "Python"
    
class Student(Course):
    # class variable
    course = "SQL"
    
    def __init__(self, name):
        self.name = name
    
    def show_student(self):
        # Accessing class variable
        print("Before")
        print("Student name:", self.name, "Course Name:", Student.course)
        
        # changing class varialbe's value
        print("Now")
        Student.course = "Machine learning"
        print("Student name", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print("Parent Class Course Name:", Course.course)

    
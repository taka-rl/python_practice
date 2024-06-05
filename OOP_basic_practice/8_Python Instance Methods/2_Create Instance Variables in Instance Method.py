class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age
    
    # instance method to add instance variable
    def add_marks(self, marks):
        # add new attribute to current object
        self.marks = marks

# create object
stud = Student(20, "Emma", 14)

# call instance method
stud.add_marks(75)

# display object
print("Roll Number:", stud.roll_no, "Name:", stud.name, "Age:", stud.age, "Marks:", stud.marks)


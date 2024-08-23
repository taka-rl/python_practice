class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age
    
    # instance method access instance variable
    def show(self):
        print("Roll Number:", self.roll_no, "Name:", self.name, "Age:", self.age)

# instance method ot modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age
    
# create object
print("class VIII")
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variable
print("class IX")
stud.update(35, 15)
stud.show()

stud.name = "Taka"
stud.show()
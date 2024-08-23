class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
stud = Student("Jessa", 20)

print("Before")
print("Name:", stud.name, "Age:", stud.age)

# modify instance variable
stud.name = "Emma"
stud.age = 15

print("After")
print("Name:", stud.name, "Age:", stud.age)

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print("Object1")
print("Name:", s1.name)
print("Age:", s1.age)

# create second object
s2 = Student("Kelly", 10)

# access instance variable
print("Object2")
print("Name:", s2.name)
print("Age:", s2.age)
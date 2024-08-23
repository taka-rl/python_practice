## Example 1: Access instance variable in the instance method

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age
        
    # instance method access instance variable
    def show(self):
        print("Name:", stud.name, "Age:", stud.age)
    
# create object
stud = Student("Jessa", 20)

# call instance method
stud.show()

## Example 2: Access instance variable using getattr()
# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))
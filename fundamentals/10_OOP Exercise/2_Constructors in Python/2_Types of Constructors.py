## Default Constructor
class Employee:
    def display(self):
        print("Inside Display")

emp = Employee()
emp.display()
print(type(emp))
# <class '__main__.Employee'>


## Non-Parametrized Constructor
class Company:
    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"
    
    # a method for printing data members
    def show(self):
        print("Name:", self.name, "Address", self.address)

# creating object of the class
cmp = Company()

# callijng the instance method using the object
cmp.show()


## Parameterrized Constructor
class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    # display object
    def show(self):
        print(self.name, self.age, self.salary)

# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()
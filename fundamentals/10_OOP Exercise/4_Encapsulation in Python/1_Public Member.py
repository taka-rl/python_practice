
## Public Member
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary
    
    # public instance methods
    def show(self):
        # accessing public data member
        print("Name", self.name, "Salary", self.salary)

# creating object of a class
emp = Employee("Jessa", 10000)

# accessing public data members
print("Name", emp.name, "Salary", emp.salary)

# calling public method of the class
emp.show()



## Overloading + operator for custom objects

'''
We can overload + operator to work with custom objects also. 
Python provides some special or magic function that is automatically invoked when associated with that particular operator.

For example, when we use the + operator, the magic method __add__() is automatically invoked. 
Internally + operator is implemented by using __add__() method. We have to override this method in our class if you want to add two custom objects.
'''

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages
    
b1 = Book(400)
b2 = Book(300)
print("Total number of pages:", b1 + b2)



## Overloading the * Operator

'''
The * operator is used to perform the multiplication. 
Let’s see how to overload it to calculate the salary of an employee for a specific period. 
Internally * operator is implemented by using the __mul__() method.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __mul__(self, timesheet):
        print("Worked for", timesheet.days, "days")
        # calculate salary
        return self.salary * timesheet.days

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is:", emp * timesheet)


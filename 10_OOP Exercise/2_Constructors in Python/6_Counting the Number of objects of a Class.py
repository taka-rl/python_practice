## Counting the Number of objects of a Class
class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1
        
# creating objects
e1 = Employee()
e2 = Employee()
e2 = Employee()
print("The number of Employee:", Employee.count)

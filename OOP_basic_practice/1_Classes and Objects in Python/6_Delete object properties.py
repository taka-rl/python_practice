class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)
        
# creating object of the class
obj = Fruit('Apple', 'red')

# Deleting object of the class
del obj.name

# Accessing Object Properties after deleting
print(obj.name) 
# Output: AttributeError: 'Fruit' object has no attribute 'name'


class Employee:
    department = "IT"
    
    def show(self):
        print("Department is", self.department)
        
emp = Employee()
emp.show()

# delete object
del emp

# Accessing after deleting object
emp.show()
# Output : NameError:name 'emp' is not defined
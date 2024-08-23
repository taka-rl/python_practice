class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)
        
# creating object of the class
obj = Fruit('Apple', 'red')

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()
# Output Fruit is strawberry and Color is red
obj.color = "pink"

obj.show()
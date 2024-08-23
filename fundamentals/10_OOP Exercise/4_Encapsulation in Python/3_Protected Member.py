# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"
        print("1")
        
# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)
        print("2")
        
    def show(self):
        print("Employee name:", self.name)
        # Accessing protected member in child class
        print("Working on project:", self._project)
        print("3")
        
c = Employee("Jessa")
c.show()

# Direct access protected data member
print("Project:", c._project)

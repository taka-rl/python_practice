'''
The @staticmethod decorator is a built-in function decorator in Python to declare a method as a static method. 
It is an expression that gets evaluated after our function is defined.
In this example, we will create a static method gather_requirement() that accepts the project name and returns all requirements to complete under this project.
Static methods are a special case of methods. 
Sometimes, you’ll write code that belongs to a class, but that doesn’t use the object itself at all. 
It is a utility method and doesn’t need an object (self parameter) to complete its operation. So we declare it as a static method. 
Also, we can call it from another method of a class.

'''

class Employee(object):
    
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name
    
    @staticmethod
    def gather_requirement(project_name):
        if project_name == "ABC Project":
            requirement = ["task_1", "task_2", "task_3"]
        else:
            requirement = ["task_1"]
        return requirement
    
    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print("Completed", task)

emp = Employee("Kelly", 12000, "ABC Project")
emp.work()

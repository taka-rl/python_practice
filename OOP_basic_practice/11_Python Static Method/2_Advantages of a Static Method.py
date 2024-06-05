'''
Here, the static method has the following advantages
・Consume Less memory:
Instance methods are object too, and creating them has a cost.
Having a static method avoids that.
Let’s assume you have ten employee objects and if you create gather_requirement() as a instance method then Python have to create a ten copies of this method (seperate for each object) which will consume more memeory. 
On the other hand static method has only one copy per class.

・To Write Utility functions:
Static methods have limited use because they don’t have access to the attributes of an object (instance variables) and class attributes (class variables). 
However, they can be helpful in utility such as conversion form one type to another. 
The parameters provided are enough to operate.

・Readabiltity:
Seeing the @staticmethod at the top of the method, we know that the method does not depend on the object’s state or the class state.

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

kelly = Employee("Kelly", 12000, "ABC Project")
jessa = Employee("Jessa", 7000, "XYZ Project")

# False
# because seperate copy of instance method is created for each object
print(kelly.work is jessa.work)
print(id(kelly.work))
print(id(jessa.work))


# True
# because only one copy is created
# kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)
print(id(kelly.gather_requirement))
print(id(jessa.gather_requirement))

# True
print(kelly.gather_requirement is Employee.gather_requirement)

'''
Output

False
2413472385920
2413472385920
True
2413472280160
2413472280160
True

'''
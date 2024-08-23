'''
Python super() function
When a class inherits all properties and behavior from the parent class is called inheritance. 
In such a case, the inherited class is a subclass and the latter class is the parent class.
In child class, we can refer to parent class by using the super() function. 
The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.

Benefits of using the super() function.
We are not required to remember or specify the parent class name to access its methods.
We can use the super() function in both single and multiple inheritances.
The super() function support code reusability as there is no need to write the entire function
'''

class Company:
    def company_name(self):
        return "Google"

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        #c_name = Company().company_name()
        # if you don't use "super() function",↑
        c_name = super().company_name()
        print("Jessa works at", c_name)
        
# Creating object of child class
emp = Employee()
emp.info()

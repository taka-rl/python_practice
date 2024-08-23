'''
Some code might use the old method of defining a static method, using staticmethod() as a function rather than a decorator.

You should only use staticmethod() function to define static method if you have to support older versions of Python (2.2 and 2.3). 
Otherwise, it is recommended to use the @staticmethod decorator.

Syntax: staticmethod(function)
function: It is the name of the method you want to convert as a static method.
It returns the converted static method.
'''

class Employee:
    def sample(x):
        print("Inside static method", x)

# convert to static method
Employee.sample = staticmethod(Employee.sample)

# call static method
Employee.sample(10)

'''
The staticmethod() approach is helpful when you need a reference to a function from a class body 
and you want to avoid the automatic transformation to the instance method.
'''


'''
Apart from a decorator, the built-in function classmethod() is used to convert a normal method into a class method. 
The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

Syntax: classmethod(function)
function: It is the name of the method you want to convert as a class method.
It returns the converted class method.

Note: The method you want to convert as a class method must accept class (cls) as the first argument, just like an instance method receives the instance (self).
As we know, the class method is bound to class rather than an object. So we can call the class method both by calling class and object.
A classmethod() function is the older way to create the class method in Python. 
In a newer version of Python, we should use the @classmethod decorator to create a class method.

'''

# Example 2: Create Class Method Using classmethod() function

class School:
    # class variable
    name = "ABC School"
    
    def school_name(cls):
        print("School Name is:", cls.name)

# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()

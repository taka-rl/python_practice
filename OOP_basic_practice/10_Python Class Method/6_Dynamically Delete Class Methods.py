'''
We can dynamically delete the class methods from the class. 
In Python, there are two ways to do it:

By using the del operator
By using delattr() method
By using the del operator

The del operator removes the instance method added by class. 
Use the del class_name.class_method syntax to delete the class method.
'''

'''
Example:
In this example, we will delete the class method named change_school() from a Student class. 
If you try to access it after removing it, you’ll get an Attribute Error.
'''

class Student:
    school_name = "ABC School"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name

jessa = Student("Jessa", 20)
print(Student.change_school("XYZ School"))
print(Student.school_name)

# delete class method
#del Student.change_school

'''
By using delatt() method

The delattr() method is used to delete the named attribute and method from the class. 
The argument to delattr is an object and string. 
The string must be the name of an attribute or method name.
'''
delattr(Student, "change_school")



# call class method
# it will give error
print(Student.change_school("PQR School"))



'''
Output

XYZ School
AttributeError: type object 'Student' has no attribute 'change_school'
'''




'''
We can dynamically delete the instance method from the class. 
In Python, there are two ways to delete method:

By using the del operator
By using delattr() method
By using the del operator

The del operator removes the instance method added by class.

'''

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def show(self):
        print("Name:", self.name, "Age:", self.age)
    
    # instance method
    def percentage(self, sub1, sub2):
        print("percentage:", (sub1 + sub2) / 2)

emma = Student("Emma", 14)
emma.show()
emma.percentage(67, 62)

#### どっちかコメントアウトして使用して！
# AttributeError: percentage occures.

# 1: Delete the method from class using del operator
del emma.percentage

# 2: delete instance method percentage() using delattr()
#delattr(emma, 'percentage')
#emma.show()

# Again calling percentage() method
# It will raise error

emma.percentage(67, 62)




'''
By using the delattr() method

The delattr() is used to delete the named attribute from the object with the prior permission of the object. 
Use the following syntax to delete the instance method.

delattr(object, name)
object: the object whose attribute we want to delete.
name: the name of the instance method you want to delete from the object.

'''


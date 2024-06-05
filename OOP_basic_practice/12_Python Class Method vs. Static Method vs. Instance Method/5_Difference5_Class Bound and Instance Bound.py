'''
Difference #5: Class Bound and Instance Bound
An instance method is bound to the object, so we can access them using the object of the class.
Class methods and static methods are bound to the class. 
So we should access them using the class name.
'''

class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no
    
    # instance method
    def show(self):
        print("In instance method")
    
    @classmethod
    def change_school(cls, name):
        print("In class method")
    
    @staticmethod
    def find_notes(subject_name):
        print("In static method")

# create an object
jessa = Student(12)

# instance method bound to object
print(jessa.show)
# class method bound to class
print(jessa.change_school)
# static method bound to class
print(jessa.find_notes)


'''
Do you know:
In Python, a separate copy of the instance methods will be created for every object.

Suppose you create five Student objects, then Python has to create five copies of the show() method (separate for each object).
So it will consume more memory.
On the other hand, the static method has only one copy per class.
'''

# create two objects
jessa = Student(12)
kelly = Student(25)

# False because two separete copies
print(jessa.show is kelly.show)

# True objects share same copies of static methods
print(jessa.find_notes is kelly.find_notes)

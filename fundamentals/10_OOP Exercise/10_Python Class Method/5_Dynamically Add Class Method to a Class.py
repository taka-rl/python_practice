'''
Typically, we add class methods to a class body when defining a class. 
However, Python is a dynamic language that allows us to add or delete methods at runtime. 
Therefore, it is helpful when you wanted to extend the class functionality without changing its basic structure because many systems use the same structure.
We need to use the classmethod() function to add a new class method to a class.

'''

class Student:
    school_name = "ABC School"
    
    print("1")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("2")
    
    def show(self):
        print(self.name, self.age)
        print("3")

    def __del__(self):
        print("4")
        print("Goodbye")
        
# class endded

# method outside class
def exercises(cls):
    # access class variables
    print("Below exercises for", cls.school_name)

# Adding class method at runtime to class
Student.exercises = classmethod(exercises)

jessa = Student("Jessa", 14)
jessa.show()

# call the new method
Student.exercises()

print(type(exercises))

'''
# output
1
2
Jessa 14
3
Below exercises for ABC School
<class 'function'>
4
Goodbye

'''


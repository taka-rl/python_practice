import time

class Student:
    #constructor
    def __init__(self, name):
        print("Inside Constructor")
        self.name = name
        
    def show(self):
        print("Hello, my name is", self.name)
    
    # destructor
    def __del__(self):
        print("Object destroyed")

# create object
s1 = Student("Emma")

# create new reference
# both reference points to the same object
s2 = s1
s1.show()
print(id(s1))
print(id(s2))

# delete object reference s1
del s1

# add sleep and observe the output
time.sleep(5)
print("After sleep")
s2.show()
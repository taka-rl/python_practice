class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age
    
    # getter method
    def get_age(self):
        return self.__age
    
    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student("Jessa", 14)

# retrieving age using getter
print("Name:", stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print("Name:", stud.name, stud.get_age())



## ↓test↓
class Student:
    def __init__(self, name, age, gender):
        # private member
        self.name = name
        self.__age = age
        self.__gender = gender
    
    # getter method
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    # setter method
    def set_age(self, age):
        self.__age = age
    
    def set_gender(self, gender):
        self.__gender = gender

stud1 = Student("Tom", 14, "Male")
stud2 = Student("Csilla", 24, "Male")

# retrieving age using getter
print("Name:", stud1.name, stud1.get_age(), stud1.get_gender())
print("Name:", stud2.name, stud2.get_age(), stud2.get_gender())

# changing age using setter
stud1.set_age(16)
stud2.set_gender("Female")

# retrieving age using getter
print("Name:", stud1.name, stud1.get_age(), stud1.get_gender())
print("Name:", stud2.name, stud2.get_age(), stud2.get_gender())


'''
Example: 
Information Hiding and conditional logic for setting an object attributes
'''
class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age
        
    def show(self):
        print("Student Details:", self.name, self.__roll_no)
        
    # getter methods
    def get_roll_no(self):
        return self.__roll_no
    
    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print("Invalid roll no. Please set correct roll number.")
        else:
            self.__roll_no = number

jessa = Student("Jessa", 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)

jessa.set_roll_no(25)
jessa.show()
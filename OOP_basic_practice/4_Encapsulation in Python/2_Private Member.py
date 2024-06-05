
## Private Member
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        # private member
        self.__salary = salary
    
    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name", self.name, "Salary", self.__salary)

# creating object of a class
emp = Employee("Jessa", 10000)

# accessing public data members
#print("Name", emp.name, "Salary", emp.__salary)
'''
↑この処理が無ければ、エラーは発生しない。
外部からクラスのprivateの値にアクセスしているため、エラー発生
'''
# calling public method of the class
emp.show()


## Public method to access private members
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        # private member
        self.__salary = salary
    
    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name", self.name, "Salary", self.__salary)

# creating object of a class
emp = Employee("Jessa", 10000)

# calling public method of the class
emp.show()


## Name Mangling to access private members
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        # private member
        self.__salary = salary
    
# creating object of a class
emp = Employee("Jessa", 10000)

print("Name", emp.name)

# direct access to private member using name magling
print("Salary", emp._Employee__salary)

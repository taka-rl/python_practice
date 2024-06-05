'''
In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute.
First, the method or attribute is searched within a class, and then it follows the order we specified while inheriting.

This order is also called the Linearization of a class, and a set of rules is called MRO (Method Resolution Order).
The MRO plays an essential role in multiple inheritances as a single method may found in multiple parent classes.
In multiple inheritance, the following search order is followed.

First, it searches in the current parent class if not available, then searches in the parents class specified while inheriting (that is left to right.)
We can get the MRO of a class. For this purpose, we can use either the mro attribute or the mro() method.

'''

class A:
    def process(self):
        print("In class A")

class B(A):
    def process(self):
        print("In class B")

class C(B, A):
    def process(self):
        print("In class C")

# Creating object of C class
c1 = C()
c1.process()
print(C.mro())

'''
In the above example, we create three classes named A, B and C. Class B is inherited from A, class C inherits from B and A. 
When we create an object of the C class and calling the process() method, Python looks for the process() method in the current class in the C class itself.
Then search for parent classes, namely B and A, because C class inherit from B and A. that is, C(B, A) and always search in left to right manner.
'''

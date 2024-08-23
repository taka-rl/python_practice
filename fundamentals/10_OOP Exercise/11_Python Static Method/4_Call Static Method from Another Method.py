'''
Let’s see how to call a static method from another static method of the same class. 
Here we will class a static method from a class method.
'''

class Test:
    @staticmethod
    def static_method_1():
        print("static method1")
        print("3")
    
    @staticmethod
    def static_method_2():
        Test.static_method_1()
        print("2")
    
    @classmethod
    def class_method_1(cls):
        cls.static_method_2()
        print("1")
        
# call class method
Test.class_method_1()

'''
Output

static method1
3
2
1
'''
'''
Difference #1: Primary Use
・Class method Used to access or modify the class state. 
It can modify the class state by changing the value of a class variable that would apply across all the class objects.
・The instance method acts on an object’s attributes. 
It can modify the object state by changing the value of instance variables.
・Static methods have limited use because they don’t have access to the attributes of an object (instance variables) and class attributes (class variables).
However, they can be helpful in utility such as conversion form one type to another.

Class methods are used as a factory method. Factory methods are those methods that return a class object for different use cases. 
For example, you need to do some pre-processing on the provided data before creating an object.

'''
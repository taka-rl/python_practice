## Constructor Chaining
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine

class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed

class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range
        
# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine = {ev.engine}, Max Speed = {ev.max_speed}, Km range = {ev.km_range}')


'''
In Python, constructor chaining is convenient when we are dealing with inheritance. 
When an instance of a child class is initialized, the constructors of all the parent classes are first invoked 
and then, in the end, the constructor of the child class is invoked.
Using the super() method we can invoke the parent class constructor from a child class.
'''
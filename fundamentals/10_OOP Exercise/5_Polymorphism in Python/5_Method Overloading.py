def addition(a, b):
    c = a + b
    print(c)

def addition(a, b, c):
    d = a + b + c
    print(d)

# the below line shows an error
# addiition(4, 5)

# This line will call the second product method
addition(3, 7, 5)

for i in range(5): print(i, end = ", ")
print()
for i in range(5, 10): print(i, end = ", ")
print()
for i in range(2, 12, 2): print(i, end = ", ")
print()

## User-defined polymorphic method
class Shape:
    # function with two default parameters
    def area(self, a, b = 0):
        if b > 0:
            print("Area of Rectangle is:", a * b)
        else:
            print("Area of Square is:", a ** 2)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5, 3)

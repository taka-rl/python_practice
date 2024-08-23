'''
Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary

Given:

showEmployee("Ben", 12000)
showEmployee("Jessa")
Expected output:

Name: Ben salary: 12000
Name: Jessa salary: 9000
'''

def showEmployee(name, salary = '9000'):
    return print("Name:", name, "salary:", salary)

showEmployee("Ben", 12000)
showEmployee("Jessa")
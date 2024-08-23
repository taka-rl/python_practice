'''
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function, 
and the function should process them and display each argument’s value.

Read: variable length of arguments in functions

Function call:

# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)

Expected Output:

Printing values
20
40
60

Printing values
80
100

'''

def func1(*args):
    for i in args:
        print(i)
    
func1(20, 40, 60)

func1(80, 100)


'''
To accept a variable length of positional arguments, i.e., 
To create functions that take n number of positional arguments we use *args as a parameter.
(prefix a parameter name with an asterisk * ).
Using this, we can pass any number of arguments to this function. 
Internally all these values are represented in the form of a tuple.

What is a Tuple?
Tuples are ordered collections of heterogeneous data that are unchangeable. Heterogeneous means tuple can store variables of all types.

Tuple has the following characteristics
Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
Unchangeable: we cannot add or delete items to the tuple after creation.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value.

'''


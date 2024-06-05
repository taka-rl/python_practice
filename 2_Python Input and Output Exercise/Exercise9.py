'''
Write a program to check 
if the given file is empty or not
'''

'''
f = open("C:\Users\is12f\Documents\programming\Python\practice\Python Input and Output Exercise\test1.txt", 'r')

string = f.read()

if len(string) == 0:
    print("The file is empty.")
else:
    print("This is not empty.")
'''

import os

size = os.stat("C:\Users\is12f\Documents\programming\Python\practice\Python Input and Output Exercise\test1.txt").st_size
if size == 0:
    print("file is empty")



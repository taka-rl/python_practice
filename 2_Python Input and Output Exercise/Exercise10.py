'''
Exercise 10: Read line number 4 from the following file
See:

Read Specific Lines From a File in Python
Python read file
Create a test.txt file and add the below content to it.

test.txt file:
line1
line2
line3
line4
line5
line6
line7
'''

# read file
with open("C:/Users/is12f/Documents/programming/Python/practice/Python Input and Output Exercise/test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 4
    print(lines[3])

print(lines[3])

    
'''
Exercise 6: Write all content of a given file 
into a new file by skipping line number 5

Create a test.txt file and add the below content to it.

Given test.txt file:
line1
line2
line3
line4
line5
line6
line7
Expected Output: new_file.txt
line1
line2
line3
line4
line6
line7

'''

import os

#making an input file
path = "C:/Users/is12f/Documents/programming/Python/practice/Python Input and Output Exercise/"

fp = open(path + 'test.txt', 'w')

for i in range(7):
    fp.write("line" + str(i+1))
    fp.write("\n")

fp.close()

#copying to another file
fp = open(path + 'test.txt', 'r')
fp1 = open(path + 'new_test.txt', 'w')

for i in fp.readlines():
    if i != 'line5\n':
        fp1.write(i)

fp.close()
fp1.close()

#--------sample answer----------

#read test.txt
with open("test.txt", "r") as fp:
    #read all lines from a file
    lines = fp.readlines()

#open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    #iterate each lines from a test.txt
    for line in lines:
        #skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            #write current line
            fp.write(line)
        #in each iteration reduce the count
        count += 1
        
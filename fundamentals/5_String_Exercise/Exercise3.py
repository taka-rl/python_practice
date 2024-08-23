'''
Exercise 3: 
Create a new string made of the first, middle, 
and last characters of each input string

Given two strings, s1 and s2, write a program 
to return a new string made of s1 and s2’s first, middle, 
and last characters.

Given:
s1 = "America"
s2 = "Japan"
Expected Output:AJrpan
'''

s1 = "America"
s2 = "Japan"

f1 = s1[0]
f2 = s2[0]

num1 = int(len(s1) / 2)
num2 = int(len(s2) / 2)
m1 = s1[num1]
m2 = s2[num2]

l1 = s1[-1]
l2 = s2[-1]

s3 = f1 + f2 + m1 + m2 + l1 + l2

print(s3)

# sample answer
def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]
    
    # get middle character from both string
    middle_char = s1[int(len(s1) / 2): int(len(s1) / 2) + 1] + s2[int(len(s2) / 2): int(len(s2) / 2) + 1]
    
    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    
    # add all
    res = first_char + middle_char + last_char
    print("Mix String is", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)

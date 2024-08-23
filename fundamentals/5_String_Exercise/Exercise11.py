'''
Exercise 11: Reverse a given string
Given:str1 = "PYnative"
Expected Output:evitanYP

'''
str1 = "PYnative"
revStr1 = str1[::-1]
print(revStr1)

# sample answer
# solution1
# 同じ

# solution2
str1 = "PYnative"
print("Original String is:", str1)

str1 = "".join(reversed(str1))
print("Reversed String is:", str1)
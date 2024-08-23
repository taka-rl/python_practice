'''
Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567
'''

num = int(input("Enter the number:"))
revNum = ""

while num > 0:
    num = num // 10
    print(num)
    revNum = revNum + str(num)

print(revNum)

# sample answer
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    print(reminder)
    reverse_number = (reverse_number * 10) + reminder
    print(reverse_number)
    num = num // 10
print("Reverse Number ", reverse_number)
    
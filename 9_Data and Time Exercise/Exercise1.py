'''
Exercise 1: Print current date and time in Python

'''

from datetime import datetime

now = datetime.now()
print("Current DateTime:", now)
print("Type:", type(now))


# sample answer
import datetime

# Print date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())
'''
Exercise 4: Print a date in a the following format
Day_name  Day_number  Month_name  Year
Refer: Python DateTime Format Using Strftime()

Given:
given_date = datetime(2020, 2, 25)
Expected output:
Tuesday 25 February 2020
'''
from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

print("New Date")
new_date = given_date.strftime("%A %d %B %Y")
print(new_date)

# sample answer
from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime("%A %d %B %Y"))
'''
Exercise 3: Subtract a week (7 days)  from a given date in Python

Given:
given_date = datetime(2020, 2, 25)

Expected output:
2020-02-18
'''
from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

print("New Date")
timeDelt = timedelta(days = 7)
print(given_date - timeDelt)

'''
https://pynative.com/python-timedelta/
Or the following way is also ok
days_to_subtract = 7
res_date = given_date - timedelta(days = days_to_subtrack)
'''

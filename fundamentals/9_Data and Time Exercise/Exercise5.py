'''
Exercise 5: Find the day of the week of a given date
Given:

given_date = datetime(2020, 7, 26)
Expected output:

Sunday
'''
from datetime import datetime

given_date = datetime(2020, 7, 26)
print("Given date")
print(given_date.strftime("%A"))

# sample answer
# solution1
from datetime import datetime
given_date = datetime(2020, 7, 26)
# To get the english name of the weekday
print(given_date.strftime("%A"))

# solution2
# using calendar module
import calendar
from datetime import datetime
given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)
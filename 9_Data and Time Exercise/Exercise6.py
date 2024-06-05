'''
Exercise 6: Add a week (7 days) and 12 hours to a given date
Given:

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
Expected output:

2020-03-29 22:00:00
'''
from datetime import datetime, timedelta
given_date = datetime(2020, 3, 22, 10, 0, 0)
# addDate = timedelta(weeks = 1, hours = 12)
addDate = timedelta(days = 7, hours = 12)
print(given_date + addDate)

'''
timedelta:
A timedelta represents a duration which is the difference between two dates, time, or datetime instances, to the microsecond resolution.
The Timedelta class available in Python’s datetime module. Use the timedelta to add or subtract weeks, days, hours, minutes, seconds, microseconds, and milliseconds from a given date and time.
'''

'''
Exercise 9: Calculate the date 4 months from the current date
Given:

# 2020-02-25
given_date = datetime(2020, 2, 25).date()
Expected output:2020-06-25
'''
from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25).date()
timeDelta = timedelta(days = 121)
#timeDelta = timedelta(months = 4)
print(given_date + timeDelta)

# sample answer

'''
We need to use the Python dateutil module’s relativedelta. We can add 4 months into the given date using a relativedelta.
The relativedelta is useful when we want to deal months with day 29, 30 31, It will properly adjust the days.
"timedelta" can be used when adding/subtracting days. However months cannot be added / subtracted by timedelta.
"relativedelta" can be used.
'''

from datetime import datetime
from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25).date()

months_to_add = 4
new_date = given_date + relativedelta(months = months_to_add)
print(new_date)

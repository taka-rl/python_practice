'''
Exercise 10: Calculate number of days between two given dates
Given:

# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)

Expected output:
205 days
'''
from datetime import datetime

# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)

print(date_1 - date_2)
print(date_2 - date_1)

# sample answer
from datetime import datetime

# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
    
else:
    print("date_2 is greater")
    delta = date_2 - date_1
    
print("Difference is", delta.days, "days")

# sample answer
date_difference = abs(date_1 - date_2)
print(date_difference.days) 
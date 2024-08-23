'''
Exercise 7: Print current time in milliseconds
'''
# sample answer
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)
'''
Use the time.time() function to get the current time in seconds 
since the epoch as a floating-point number.
'''

'''
As there is no formatting code available for milliseconds, 
we can only display it using the %S code. 
However, as milliseconds are 3 decimal places away from seconds, 
we can display that information by combining %S with %f.

'''
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# [:-3]:3桁表示


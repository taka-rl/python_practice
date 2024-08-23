'''
Exercise 2: Convert string into a datetime object
For example, You received the following date in string format. 
Please convert it into Python’s DateTime object.
Refer: Python String to DateTime
Given:
date_string = "Feb 25 2020 4:20PM"
Expected output:
2020-02-25 16:20:00
'''
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"

# dt_object = datetime.strptime(date_string, "%Y%b%d  %H:%M:%S")
dt_object = datetime.strptime(date_string, "%b %d %Y %H:%M%p")
print(dt_object)

'''
Directive	Description	Example
%d	Day of the month as a zero-padded decimal number.	Sun, Mon, …, Sat (en_US);
So, Mo, …, Sa (de_DE)
%m	Month of the year as a zero-padded decimal number.	Sunday, Monday, …, Saturday (en_US);
Sonntag, Montag, …, Samstag (de_DE)
%Y	A year with a century in four-digit format	0001, 2021, … , 9999
%y	A year without a century in two-digit format	01, 21, …, 31
%A	Full name of a weekday as per the locale’s name.
Sunday, …, Saturday (en_US);
Sonntag, …, Samstag (de_DE)
%a	Short name of a weekday as the locale’s abbreviated name.	Sun, …, Sat (en_US);
So, …, Sa (de_DE)
%B	Full name of a month as per the locale’s name	January, …, December (en_US);
Januar, …, Dezember (de_DE)
%b	Short name of a month as the locale’s abbreviated name.	Jan, …, Dec (en_US);
Jan, …, Dez (de_DE)
%H	Hour (24-hour clock) as a zero-padded decimal number.	01, 02, … , 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12
%p	Locale’s equivalent of either AM or PM.	AM, PM (en_US);
am, pm (de_DE)
%M	Minute as a zero-padded decimal number.	00, 01, …, 59
%S	Second as a zero-padded decimal number.	00, 01, …, 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000, 000001, …, 999999
%z	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).	(empty), +0000, -0400, +1030, +063415, -030712.345216
%Z	Time zone name (empty string if the object is naive).
(empty), UTC, GMT
%j	Day of the year as a zero-padded decimal number.	001, 002, …, 366
%U	Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, …, 53
%W	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, …, 53
%c	Locale’s appropriate date and time representation.	Tue Aug 16 21:30:00 1988 (en_US);
Di 16 Aug 21:30:00 1988 (de_DE)
%x	Locale’s appropriate date representation.	08/16/88 (None);
08/16/1988 (en_US);
16.08.1988 (de_DE)
%X	Locale’s appropriate time representation.	21:30:00 (en_US);
21:30:00 (de_DE)
%%	A literal '%' character.

'''
# Task :
#
# Calendar of the curent year.
# Also mention whether a given year or not
# From the current leap year to next leap year calculate the number of dates

import calendar
from datetime import date

year = int(input('Enter Year : '))

cal = calendar.calendar(year,2,1,6)
leap_year = calendar.isleap(year)

if(leap_year == True):
    d1 = date(year+5,1,1)
    d2 = date(year,1,1)
    total_days = d1-d2
    print('Calendar of year',year,' :\n',cal)
    print(year,' is a Leap Year\n')
    print('Total No. of days from Current Leap Year to Next Leap Year : ',total_days.days)

else:
    print('Calendar of year',year,' :\n',cal)
    print(year,' is not a Leap Year')

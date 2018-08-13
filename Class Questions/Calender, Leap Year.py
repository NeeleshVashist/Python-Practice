# Task :
#
# Calendar of the curent year.
# Also mention whether a given year or not
# From the current leap year to next leap year calculate the number of dates

import calendar

year = int(input('Enter Year : '))

cal = calendar.calendar(year,2,1,6)
leap_year = calendar.isleap(year)

if(leap_year == True):
    total_days = (365 * 3) + (366 * 2)
    print('Calendar of year',year,' :\n',cal)
    print(year,' is a Leap Year\n')
    print('Total No. of days from Current Leap Year to Next Leap Year : ',total_days)

else:
    print('Calendar of year',year,' :\n',cal)
    print(year,' is not a Leap Year')

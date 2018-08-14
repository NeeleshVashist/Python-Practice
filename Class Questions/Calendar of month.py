# Task :
#
# Display the calender of current month and days of the first week
# Also display the week day

import calendar
import datetime

year = int(input('Enter Year : '))
month = int(input('Enter Month : '))
date = int(input('Enter Date : '))

#To get the calendar of year
m = calendar.month(year,month,2,1)

#weekday is used to get day number
d = calendar.weekday(year,month,date)

#strftime("%a, %d. %B, %y"  -> %a = day, %d = date, %B = Month, %y = Year)
now = datetime.datetime.now()
day = now.strftime("%a")

print(f'Calander of {month}th of Year {year} :\n',m)
print(f'Weekday Number for {date} of {month}th of {year} : ',d)
print(f'Day of {date} of {month}th of {year} : '+day)

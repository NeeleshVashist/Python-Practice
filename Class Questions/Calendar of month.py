# Task :
#
# Display the calender of current month and days of the first week
# Also display the week day

import calendar
import datetime

year = int(input('Enter Year : '))
month = int(input('Enter Month : '))
date = int(input('Enter Date : '))

m = calendar.month(year,month,2,1)
d = calendar.weekday(year,month,date)

if(d == 0):
    d = 'Monday'
elif(d == 1):
    d = 'Tuesday'
elif(d == 2):
    d = 'Wednesday'
elif(d == 3):
    d = 'Thusday'
elif(d == 4):
    d = 'Friday'
elif(d == 5):
    d = 'Saturday'
elif(d == 6):
    d = 'Sunday'

print(f'Calander of {month}th of Year {year} :\n',m)
print(f'Weekday Number for {date} of {month}th of {year} : '+d)

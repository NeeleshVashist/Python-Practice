# Task
# You are given the year, and you have to write a function to check if the year is
# leap or not.
#
# Note that you have to complete the function and remaining code is given as
# template.

def is_leap(year):
    leap = False

    # Write your logic here

    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                leap = True
        else:
            leap = True

    return leap

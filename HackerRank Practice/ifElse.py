# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())

if (n%2==1):
    print('Weird')
elif(n%2==0 and (n==2 or n==4 or n>20)):
    print('Not Weird')
elif(n%2==0 and (n>5 or n<21)):
    print('Weird')

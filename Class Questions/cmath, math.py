# Task :
#
# Write a program that takes a input of the real and imaginary part and prints it complex number
# Also display the complex number with base b

import cmath
import math

x = float(input('Enter X(First real Number) : '))
y = float(input('Enter X(Second real Number) : '))
l = int(input('Enter Base : '))

# converting x and y into complex number
z = complex(x,y);

# converting complex number into polar using polar()
w = cmath.polar(z)

#Making List
my_list = list(w)

# converting complex number into rectangular using rect()
w = cmath.rect(my_list[0], my_list[1])

#log() returns natural logarithm of x, for x > 0.
base_log = cmath.log(z,l)


#printing statements
print ("The modulus and argument of polar complex number is : ",w)

print ("The rectangular form of complex number is : ",end="")
print (w)

print(f"The log(base {l}) of complex number is : ", end="")
print(base_log)

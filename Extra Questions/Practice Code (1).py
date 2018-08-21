# Task :
#
# A non-negative integer is entered through the keyboard. Check whether the given
# integer is palindrome number or not.
# If the given integer is palindrome then display the sum of digits of given integer.
# If the given integer is not palindrome then display the no. of digits in given integer
# Sample Input1:
# 121	#input number
# Sample Output1:
# 4	#since it is a palindrome, sum of digits: 1+2+1=4

n = input('Enter Number : ')
num = int(n)
sum = 0

rev = n[::-1]

if(rev == n):
    for i in range(len(n)):
        sum = sum + int(n[i])

    print('Sum is :',sum)

else:
    print('Length is:',len(n))

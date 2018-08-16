# Task :
#
# Given the list of n numbers contains positive and negative values.
# Write a program using modules :
#     - to find unique triples whose 3 elements gives the sum 0 from the given numbers
#     - form the given list find the possible 2 digit valid numbers
#     - find a random number which can be both positive and negative from the sepicified range entered by the user

import unique_triplets, valid_numbers, random_numbers

def list_maker():
    n = int(input('Enter the List Size : '))
    my_list = []

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    return my_list

if __name__ == '__main__':

    print('Enter your choice : ')
    print('1 for finding triplets with sum 0')
    print('2 for finding 2 digit valid numbers')
    print('3 for finding a random number')

    choice = int(input('Enter your choice : '))

    while(choice < 1 or choice > 3):
        print('Wrong Choice Entered...TRY AGAIN')
        choice = int(input('Enter your choice : '))

    if(choice == 1):
        my_list = list_maker()
        unique_triplets.triplets(my_list)

    elif(choice == 2):
        my_list = list_maker()
        valid_numbers.validate(my_list)

    elif(choice == 3):
        print('Enter Range : ')
        a = int(input('Enter 1st number of range : '))
        b = int(input('Enter 2nd number of range : '))
        random_numbers.rand_no(a,b)

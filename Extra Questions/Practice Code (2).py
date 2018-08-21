# Task :
#
# A List of Flowers
#
# There is bunch of flowers available where each flower is tagged by a number. Ram
# randomly picked up the flowers that might contain duplicate tag numbers. Now, he
# has to form a bouquet from that picked up flowers such that each bouquet contains
# the flowers with unique tag numbers. He has to perform this action every time a
# bouquet is to be prepared. So, he thought of automating this process. Help Ram to
# automate this process so that he can perform this task fastly.
# Write a program using functions that takes List as input which contains duplicate
# tag numbers. The task is to remove the duplicate tag numbers i.e. to form a new
# list that contains unique tag numbers.
#
# If the list is empty, do display the message: "List is empty".
#
# Explanation:
# First Line of the input contains the number of elements in the list.
# Next Lines refers to the elements of the list to be entered.
# Sample Input:
# 5
# 1
# 2
# 3
# 1
# 4
# Sample Output:
# [1, 2, 3, 4]

def count(my_list):

    if(my_list == []):
        print('List is Empty')
    else:
        my_list = list(set(my_list))

        print('List is :',my_list)

if __name__ == '__main__':
    n = int(input('Enter Number of Elements : '))
    my_list = []

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    count(my_list)

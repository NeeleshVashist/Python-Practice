# Task :
#
# A list of numbers is provided to the students such that there are required to
# sort the list according to length of its elements.
# Assume that all the elements of the list are integers.
# Print the output in the required format
#
# Sample Input :
# T.C 1 -> [23,10,4566,344,123,121]
# T.C 2 -> [2,3,10,1,3,123]
# T.C 3 -> [111,101,9,3,123,1431,19]
#
# Sample Output :
# T.C 1 -> [23,10,344,123,121,4566]
# T.C 2 -> [2,3,1,3,10,123]
# T.C 3 -> [9,3,19,111,101,123,1431]
#
# Constraint :
# Max Length of Element : 4

def sort_list(my_list):
    new_list = []
    length_of_element = 4

    for j in range(1,length_of_element+1):
        for i in range(len(my_list)):
            if(len(str(my_list[i])) == j):
                new_list.append(my_list[i])

    print(f'Sorted List according to Length of Elements : {new_list}')


if __name__ == '__main__':
    my_list = []

    n = int(input('Enter List Length : '))

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    sort_list(my_list)

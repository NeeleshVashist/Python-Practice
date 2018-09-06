# Task :
#
# Given an array of n integers, also there are two distroying sets
# set a and set b
#
# Set a and b contains m int each.
# You like all the int in set a and dislike all the int of set b.
#
# Your initial happiness is zero, for each i int in the array, if i belongs to a
# then you add 1 to your happiness, if i belongs to b then you add -1 t your array.
# Otherwise, your happiness does not change.
#
# Output final happiness.
#
# I/P Format :
#     First Line contains, n and m in seperated by space
#     Second line contains, n int that is the elements of array
#     Third and fouth lines contains m int of a and b respectively
#
# Sample I/P :
#     3 2
#     1 5 3
#     3 1
#     5 7
#
# Sample O/P :
#     1


if __name__ == '__main__':
    n_m = input('Enter n and m(seperated by space) : ').split()

    n = int(n_m[0])
    m = int(n_m[1])
    my_list = []
    set_a = []
    set_b = []
    count = 0

    print('\n******************************************\n')

    print('Enter Array Elements : ')
    num_array = input('Enter Element(seperated by space) : ').split()
    for i in range(len(num_array)):
        my_list.append(int(num_array[i]))

    print('\n******************************************\n')

    print('Enter Set A Elements : ')
    num_a = input('Enter Element(seperated by space) : ').split()
    for i in range(len(num_a)):
        set_a.append(int(num_a[i]))

    print('\n******************************************\n')

    print('Enter Set B Elements : ')
    num_b = input('Enter Element(seperated by space) : ').split()
    for i in range(len(num_b)):
        set_b.append(int(num_b[i]))


    for i in range(len(set_a)):
        if set_a[i] in my_list:
            count += 1
        if set_b[i] in my_list:
            count -= 1

    print(f'Happiness Count : {count}')

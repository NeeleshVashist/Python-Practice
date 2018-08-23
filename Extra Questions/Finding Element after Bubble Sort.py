# Task :
#
# Of the given list of elements find the kth element in the list sorted by bubble sort
# machinism


def bubble_sort(my_list,n):

    for i in range(n):
        for j in range(n):
            if(my_list[i] < my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return(my_list)

def kth_element(my_list):
    n = len(my_list)
    new_list = bubble_sort(my_list,n)
    k = int(input('Enter Position to find : '))

    print(f'kth Element is : {new_list[k]}')


if __name__ == '__main__':
    my_list = []
    n = int(input('Enter List Length : '))

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    kth_element(my_list)

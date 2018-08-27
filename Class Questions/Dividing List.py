# Task :
#
# Input : [1,2,3,4,5,6]
# Output : [4,5,6,1,2,3]

if __name__ == '__main__':
    my_list = []
    n = int(input('Enter List Size : '))

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    length = len(my_list)
    list1 = my_list[length//2:]
    list2 = my_list[:length//2]

    final_list = list1 + list2
    print(f'Final List : {final_list}')

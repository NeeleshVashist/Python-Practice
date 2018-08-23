# Task :
#
# Find the occurence of each element in the list

if __name__ == '__main__':

    my_list = []
    count = 1
    n = int(input('Enter List Size : '))

    for i in range(n):
        num = int(input('Enter Number : '))
        my_list.append(num)

    my_list.sort()

    for i in range(n-1):
        if(my_list[i] == my_list[i+1]):
            count += 1
        else:
            print(my_list[i],'occurs', count,'times')
            count=1

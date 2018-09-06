# Task :
#
# Find the length of subparts of a number and find the duplicates in between those subparts
#
# Sample I/P :
#     num (Length of number)
#     n (Length of substring)
#
# Sample O/P :
#     Count of substrings
#     No of duplicates in 1st subpart :
#     |
#     |
#     |

if __name__ == '__main__':
    my_list = []
    new_count = 0
    count = 0

    num = input('Enter Number(Min Length : 5, Max Length : 20) : ')
    while(len(num) <= 5 and len(num) >= 20):
        print('Enter Again...Min Length : 5, Max Length : 20')
        num = input('Enter Number : ')

    n = int(input('Enter Length of Sub-Part : '))

    count = (len(num) - n) + 1

    for i in range(count):
        new_num = int(num[i:i+n])
        my_list.append(new_num)

    print(f'Total number of subparts : {count}')
    
    for i in range(len(my_list)):
        dup = len(set(str(my_list[i])))
        new_count = (len(str(my_list[i])) - dup)
        print(f'No. of duplicates in {my_list[i]} : {new_count}')
        count = 0

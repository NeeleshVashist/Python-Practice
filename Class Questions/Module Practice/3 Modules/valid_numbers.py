# Task :
#
# form the given list find the possible 2 digit valid numbers

def validate(my_list):
    n = len(my_list)
    found = False

    for i in range(n):
        if(my_list[i] >= 10 and my_list[i] <= 99):
            print(my_list[i])
            found = True

    if(found == False):
        print('No 2 digit unique number found')

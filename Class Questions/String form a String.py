count = 0
new_str = ''
new_str2 = ''
st = input('Enter a String : ')
my_str = st[::-1]

if(len(st) < 3):
    print('String is Empty :',new_str)

elif(len(st) == 4):
    new_str = str
    print('String is :',new_str)

else:
    # for i in range(len(st)):
    #     if(i < 2):
    #         new_str = new_str + st[i]
    #         count += 1
    #         if(count > 2):
    #             break
    #
    # count = 0
    #
    # for i in range(len(my_str)):
    #     if(i < 2):
    #         new_str2 = new_str2 + my_str[i]
    #         count += 1
    #         if(count > 2):
    #             break
    #
    # new_str2 = new_str2[::-1]
    # new_str = new_str + new_str2

    new_str = st[0:2]
    new_str = new_str + st[-2:]

    print('String is :',new_str)

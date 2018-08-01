first_dic = {1 : 1000, 2 : 2000, 3 : 3000, 4 : 4000, 5 : 5000, 6 : 6000, 7 : 7000, 8 : 8000, 9 : 9000, 10 : 10000}
second_dic = {1000 : 1000000, 2000 : 2000000, 3000 : 3000000, 4000 : 4000000, 5000 : 5000000, 6000 : 6000000, 7000 : 7000000, 8000 : 8000000, 9000 : 9000000, 10000 : 10000000}

# print('Choose from given options :')
# print('1 for KM to M')
# print('2 for M to CM')
# print('3 for KM to CM')
#
# option = 0
# cin>>option
#
# if(option<1 or option>4):
#     print('Invalid Option')
#
# else

km = int(input('Enter KM : '));

for a,b in first_dic.items():
    for x,y in second_dic.items():
        if(a == km):
            if(b == x):
                print(km,'KM in CM : ',y)

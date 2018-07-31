r = int(input('Enter the No. of Students : '))
my_list = []
my_dic = {}
final_dic = {}
sum = 0

for i in range(r):
    name = input('Enter Name : ')
    num = int(input('Enter how many subjects : '))

    for j in range(num):
        x = int(input('Enter Marks : '))
        my_list.append(x)
        sum += x

    my_dic[name] = my_list
    final_dic[name] = sum
    sum = 0
    my_list = []

print('Dictionary is :',my_dic)
print('Total :',final_dic)

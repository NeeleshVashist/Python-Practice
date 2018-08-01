#Sum of 2d matrix

list1 = []
list2 = []
list3 = []
sub_list = []
main_list = []

m = int(input('Enter Number of Rows : '))
n = int(input('Enter Number of columns : '))

for i in range(0,m):
    for j in range(0,n):
        a = int(input('Enter a Number for first matrix: '))
        sub_list.append(a)

    list1.append(sub_list)
    sub_list = []

print('*************************************')

for i in range(0,m):
    for j in range(0,n):
        a = int(input('Enter a Number for second matrix : '))
        sub_list.append(a)

    list2.append(sub_list)
    sub_list = []

for i in range(0,m):
    for j in range(0,n):
        sub_list.append(list1[i][j] + list2[i][j])

    list3.append(sub_list)
    sub_list = []

print('First List : ',list1)
print('Second List : ',list2)
print('Final List : ',list3)

my_tuple = ()
my_list = []

num = int(input('Enter no. of items : '))

for i in range(num):
    x = input('Enter Item : ')
    my_list.append(x)

my_tuple = tuple(my_list)

print('Tuple :',my_tuple)

find = input('Enter Item to find its index : ')

count = my_tuple.index(find)

print('Index is :',count)

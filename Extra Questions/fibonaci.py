a = 0
b = 1
c = 0
fibonaci_list = []

num = int(input('Enter how many iterations you want : '))

fibonaci_list.append(a)
fibonaci_list.append(b)

for i in range(2,num):

    c = a + b
    fibonaci_list.append(c)

    a = b
    b = c

print('List is : ',fibonaci_list)

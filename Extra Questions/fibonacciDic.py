#Fibonacci Series in Dictionary

first_dic = {}
a = 0
b = 1

num = int(input('Enter number of iterations : '))

first_dic[0] = a
first_dic[1] = b

for i in range(2,num):
    c = a+b

    first_dic[i] = c

    a = b
    b = c

print('Fibonacci Dictionary :',first_dic)

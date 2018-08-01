my_dic = {}
flag = 1

print('Enter -1 to EXIT')

num = int(input('Enter Radius : '))

while(num != -1):

    cir = 2*3.14*num
    my_dic[num] = cir

    num = int(input('Enter Radius : '))

print('Dictionary is :',my_dic)

s = int(input('Enter Radius to find its Circumference : '))

for a,b in my_dic.items():
    if(a == s):
        print('Circumference is :',b)
        flag = 1
        break
    else:
        flag = 0

if(flag == 0):
    print('Radius not found in Dictionary')

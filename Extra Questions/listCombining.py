final_list = []
list1 = []
list2 = []

num1 = int(input('How many Words you wanna enter in List1 : '))

for i in range(num1):
    input1 = input('Enter Word : ')
    list1.append(input1)

num2 = int(input('How many Words you wanna enter in List2 : '))

for i in range(num2):
    input2 = input('Enter Word : ')
    list2.append(input2)

x = num1*num2
# y, z = 0, 0
# sy, sz = num1, num2
list3 = []
list4 = []
count = 0

for j in range(x):
    for i in range(num1):
        for j in range(num2):
            list3.append(list1[i])
            list3.append(list2[j])

            elements = ''.join(list3)
            count += 1
            if(count < x+1):
                list4.append(elements)

            list3 = []

print('Combined List :',list4)

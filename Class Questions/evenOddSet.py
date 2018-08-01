even_set = set({})
odd_set = set({})
main_list = []

num = int(input('How many numbers you want to enter : '))

for i in range(num):
    no = input('Enter Number/String : ')
    main_list.append(no)

    if(i%2 == 0):
        even_set.add(no)
    else:
        odd_set.add(no)

print('Main List :',main_list)
print('Even Set :',even_set)
print('Odd Set :',odd_set)

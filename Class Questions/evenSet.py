main_set = set({})
even_set = set({})

num = int(input('Enter how many numbers you want : '))

for i in range(num):
    x = int(input('Enter a number : '))
    main_set.add(x)

    if(x%2 == 0):
        even_set.add(x)

print('Main Set :',main_set)
print('Even Set :',even_set)

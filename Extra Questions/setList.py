num = int(input('Enter the size of list : '))
my_list = set({})
even_list = set({})
odd_list = set({})
prime_list = set({})

for i in range(num):
    no = int(input('Enter a Number : '))
    my_list.add(no)

my_list = set(my_list)

for i in my_list:
    if(i%2 == 0):
        even_list.add(i)

    else:
        odd_list.add(i)

        if(i>1):
            for j in range(2,i):
                #print(i,j)
                if(i%j == 0):
                    break
            else:
                prime_list.add(i)

if(even_list == set()):
    even_list = {'No Element present'}

elif(odd_list == set()):
    odd_list = {'No Element present'}

elif(prime_list == set()):
    prime_list = {'No Element present'}

print('My List :',my_list)
print('Even List :',even_list)
print('Odd List :',odd_list)
print('Prime List :',prime_list)

# str = input('Enter a string : ')
#
# str = str.swapcase()
#
# print('String is :',str)

str = input('Enter a string : ')
new_str = ''
count = 0

for i in str:

    if(i.islower() == True):
        b = i.upper()
        count += 1
        new_str = new_str + b
    else:
        b = i.lower()
        count += 1
        new_str = new_str + b

print('String is :',new_str)

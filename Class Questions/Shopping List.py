my_list = []

print('Just press Enter to Exit')
s = input('Enter name of Item : ')
s = s.capitalize()

while(s != ''):
    my_list.append(s)

    s = input('Enter name of Item : ')
    s = s.capitalize()


print('Shopping List :',my_list)

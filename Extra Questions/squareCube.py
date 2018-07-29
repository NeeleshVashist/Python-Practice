m = int(input('Enter m : '))
n = int(input('Enter n : '))

sq_list = []
cube_list = []

for i in range(m,n):
    sq_list.append(i**2)
    cube_list.append(i**3)

print('Square List :',sq_list)
print('Cube List :',cube_list)

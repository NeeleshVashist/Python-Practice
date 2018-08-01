#Input leni h kitni cities leni h names print it in sorted form

num = int(input('Enter how many cities to add : '))
cities = []

for i in range(num):
    city = input('Enter City : ')
    cities.append(city)

cities.sort()

print('Cities are :',cities)

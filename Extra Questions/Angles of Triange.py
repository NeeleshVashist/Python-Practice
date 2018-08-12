# Task :
#
# Find the angles of a triangle

from math import acos, degrees, sqrt

if __name__ == '__main__':
    n = 3
    my_list = []
    new_list = []
    side_list = []

    for i in range(n):
        coordinates = input('Enter Coordinates(separated by a space) : ')
        coordinates = coordinates.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        new_list.append(x)
        new_list.append(y)
        my_list.append(new_list)
        new_list = []

    print('\nEntered Coordinates are :',my_list)

    x1 = my_list[0][0]
    x2 = my_list[1][0]
    x3 = my_list[2][0]
    y1 = my_list[0][1]
    y2 = my_list[1][1]
    y3 = my_list[2][1]

    #Finding Lengths of Sides
    A = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    B = sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))
    C = sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    #Finding Angles
    alpha_angle = degrees(acos(((A ** 2) + (B ** 2) - (C ** 2))/(2.0 * A * B)))
    beta_angle = degrees(acos(((B ** 2) + (C ** 2) - (A ** 2))/(2.0 * B * C)))
    gamma_angle = degrees(acos(((C ** 2) + (A ** 2) - (B ** 2))/(2.0 * C * A)))

    if(alpha_angle == 180 or beta_angle == 180 or gamma_angle == 180):
        print('\nEntered coordinates are not forming triangle')
    else:
        print('\nAngles are : ')
        print('Alpha :',round(alpha_angle))
        print('Beta :',round(beta_angle))
        print('Gamma :',round(gamma_angle))

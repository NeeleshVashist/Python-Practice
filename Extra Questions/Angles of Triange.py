# Task :
#
# Find the angles of a triangle

from math import acos, degrees, sqrt

if __name__ == '__main__':
    n = int(input('Enter No. of Coordinates : '))
    my_list = []
    new_list = []
    coordinate_list = []
    angle_list = []
    side_list = []

    while(n < 3):
        print('Minimum 3 Coordinates required')
        print('TRY AGAIN')
        n = int(input('Enter No. of Coordinates : '))

    for i in range(n):
        coordinates = input('Enter Coordinates(separated by a space) : ')
        coordinates = coordinates.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        new_list.append(x)
        new_list.append(y)
        my_list.append(new_list)
        new_list = []

    X = my_list[-2][0] + 1
    Y = my_list[-2][0] + 1
    coordinate_list.append(X)
    coordinate_list.append(Y)
    angle_list.append(coordinate_list)
    angle_list.append(my_list[-2])
    angle_list.append(my_list[-1])

    x1 = angle_list[0][0]
    x2 = angle_list[1][0]
    x3 = angle_list[2][0]
    y1 = angle_list[0][1]
    y2 = angle_list[1][1]
    y3 = angle_list[2][1]

    #Finding Lengths of Sides
    A = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    B = sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))
    C = sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    #Finding Angles
    alpha_angle = degrees(acos(((A ** 2) + (B ** 2) - (C ** 2))/(2.0 * A * B)))
    beta_angle = degrees(acos(((B ** 2) + (C ** 2) - (A ** 2))/(2.0 * B * C)))
    gamma_angle = degrees(acos(((C ** 2) + (A ** 2) - (B ** 2))/(2.0 * C * A)))

    print(round(alpha_angle), round(beta_angle), round(gamma_angle))

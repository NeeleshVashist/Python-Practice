'''
TASK :

Taxis of Kharagpur are famous for making sharp turns. You are given the coordinates where
a particular taxi was on a 2-D planes at N different moments: (x1, y1), (x2, y2), ...,
(xN, yN).
In between these coordinates, the taxi moves on a straight line. A turn at the
i-th (2 ≤ i ≤ N-1) coordinate is said to be a sharp turn if the angle by which it turns
at Point B = (xi, yi) when going from coordinates A = (xi-1, yi-1)to C = (xi+1, yi+1)
via (xi, yi) is greater than 45 degrees. ie. suppose you extend the line segment AB
further till a point D, then the angle DBC would be greater than 45 degrees.You have to
identify whether the taxi made a sharp turn somewhere or not (Please look at Output
section for details). If it made a sharp turn, also identify whether it is possible to
change the coordinates at one of the N moments to make sure that the taxi doesn't make
any sharp turn. Note that all the N pairs of coordinates (including the new coordinates)
should be integers and distinct and should have their x and y coordinates at least 0 and
at most 50.


INPUT :

    The first line of the input contains a single integer T denoting the number
    of test cases.
    The description of T test cases follows.
    The first line of each test case contains a single integer N denoting the
    number of moments at which you are given the information of the taxi's
    coordinates.
    Each of the next N lines contains two space-separated integers xi and yi
    denoting the x and y coordinates of the taxi at i-th moment.


OUTPUT :

    For each test case, print a single line containing two space-separated
    strings, either of which can be a "yes" or "no" (without quotes).
    If there was no sharp turn, the first string should be "yes", and if there
    was a sharp turn, the first string should be "no".
    For the second string, you should tell whether it is possible to modify at
    most one coordinate in such a way that taxi doesn't make a sharp turn.
    Note that if the first string is "yes", then the second string would always
    be "yes".


CONSTRAINTS :

    1 ≤ T ≤ 50
    3 ≤ N ≤ 50
    0 ≤ xi, yi ≤ 50

It's guaranteed that all (xi, yi) pairs are distinct.


EXAMPLE :

******Input******
5
3
0 0
1 1
2 1
3
0 0
1 0
6 1
3
0 0
1 0
1 1
4
0 0
1 0
1 1
6 1
6
0 0
1 0
1 1
2 1
2 2
3 2

******Output******
yes yes
yes yes
no yes
no yes
no no
'''

from math import acos, degrees, sqrt

if __name__ == '__main__':

    test_case = int(input('Enter Nummber of Test Cases : '))

    my_list = []
    new_list = []
    coordinate_list = []
    angle_list = []
    side_list = []

    for i in range(test_case):
        no_of_coordinates = int(input('Enter No. of Coordinates : '))

        while(no_of_coordinates < 3 or no_of_coordinates > 50):
            print('Minimum 3 and Maximum 50 Coordinates required')
            print('TRY AGAIN')
            no_of_coordinates = int(input('Enter No. of Coordinates : '))

        for j in range(no_of_coordinates):
            coordinates = input('Enter Coordinates(separated by a space) : ')
            coordinates = coordinates.split()
            x = int(coordinates[0])
            y = int(coordinates[1])
            new_list.append(x)
            new_list.append(y)
            my_list.append(new_list)
            new_list = []

        diff_x = my_list[-2][0] - my_list[-3][0]
        diff_y = my_list[-2][1] - my_list[-3][1]

        X = my_list[-2][0] + diff_x
        Y = my_list[-2][1] + diff_y

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
        angle = degrees(acos(((A ** 2) + (B ** 2) - (C ** 2))/(2.0 * A * B)))

        # print(angle_list)
        # print(angle)
        coordinate_list = []
        angle_list = []

        if(angle <= 45):
            print('yes yes')
        else:
            print('no')

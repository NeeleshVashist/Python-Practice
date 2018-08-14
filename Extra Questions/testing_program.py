from math import acos, degrees, sqrt

if __name__ == '__main__':

    test_case = int(input('Enter Nummber of Test Cases : '))

    my_list = []
    new_list = []
    coordinate_list = []
    angle_list = []
    side_list = []
    modified_list = []
    st = ''
    count = 0

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

        COUNT = 1
        # print(my_list)

        for k in range(COUNT,no_of_coordinates - 1):
            modified_list = my_list[k-1:k+2]
            diff_x = modified_list[-2][0] - modified_list[-3][0]
            diff_y = modified_list[-2][1] - modified_list[-3][1]

            X = modified_list[-2][0] + diff_x
            Y = modified_list[-2][1] + diff_y

            coordinate_list.append(X)
            coordinate_list.append(Y)
            angle_list.append(coordinate_list)
            angle_list.append(modified_list[-2])
            angle_list.append(modified_list[-1])

            # print(my_list[k-1:k+2])
            # print('modified_list :',modified_list)
            # print('angle_list :',angle_list)

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

            #Finding Angle
            angle = degrees(acos(((A ** 2) + (B ** 2) - (C ** 2))/(2.0 * A * B)))

            # print(angle_list)
            # print(angle)
            coordinate_list = []
            angle_list = []
            modified_list = []
            # my_list = []

            if(angle <= 45):
                # print('OK')
                flag = 1
            else:
                # print('NOT OK')
                flag = 0
                count += 1
                # print(count)

        if(flag == 1):
            st += 'yes yes\n'
        elif(count <= 2):
            st += 'no yes\n'
        elif(count > 2):
            st += 'no no\n'

        count = 0
        my_list = []

    print('\n**********************************')
    print(st)

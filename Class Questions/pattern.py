def pattern():
    for i in range(len(str)):
        if(char == str[i]):
            x = i;
            my_list.append(x)

    for i in range(len(str)):
        if(i != x):
            print(str[:i+1])
        elif(x == i):
            break

if __name__ == '__main__':
    str = input('Enter a String : ')
    char = input('Enter a single character : ')
    my_list = []

    while(len(char) != 1):
        print('Wrong character entered')
        char = input('Enter a single character : ')

    pattern()

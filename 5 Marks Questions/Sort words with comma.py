# Task :
#
# Write a program that accepts comma separated sequence of words as input and print
# the words in comma seperated sequence after sorted them in alphabetical order
#
# Sample Input :
# without,hello,would,bye
#
# Sample Output :
# bye,hello,without,would

if __name__ == '__main__':
    string = input('Enter String : ').split(',')
    string.sort()

    print(string[0],end='')
    for i in range(1,len(string)):
        print(f',{string[i]}',end='')

    print()

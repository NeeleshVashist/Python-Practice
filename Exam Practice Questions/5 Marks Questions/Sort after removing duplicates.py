# Task :
#
# WAP that accepts whitespace separated words as input and print the words after removing
# all dulplicating words and sorts them alphanumerically
#
# Sample Input :
# hello world practice makes perfect and hello world again
#
# Sample Output :
# again and hello makes perfect practice world

if __name__ == '__main__':
    string = input('Enter String(with space) : ').split()

    string = list(set(string))
    string.sort()

    print('Required Output : ',end='')
    for i in range(len(string)):
        print(f'{string[i]} ',end='')

    print()

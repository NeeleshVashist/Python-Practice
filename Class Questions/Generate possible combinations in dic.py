# Task :
#
# Strings : {1:'abc', 2:'def', 3:'ghi', 4:'jkl', 5:'mno', 6:'pqrs', 7:'tuv', 8:'wxy', 9:'z'}
#
# Given the dictionary strings generate all possible two digit letter combinations
# from the digit 1 to 9.

if __name__ == '__main__':
    Strings = {1:'abc', 2:'def', 3:'ghi', 4:'jkl', 5:'mno', 6:'pqrs', 7:'tuv', 8:'wxy', 9:'z'}
    num = input('Enter two numbers(from 1 to 9) : ')
    my_list = []

    num_1 = Strings[int(num[0])]
    num_2 = Strings[int(num[1])]

    for i in range(len(num_1)):
        for j in range(len(num_2)):
            my_list.append(num_1[i]+num_2[j])

    print(f'Required Output : {my_list}')

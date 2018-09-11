# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
#
# Then, the output should be:
#
# again and hello makes perfect practice world

if __name__ == '__main__':
    new_str = ' '
    my_string = input('Enter a String : ').split()
    my_string = list(set(my_string))
    my_string.sort()

    my_string = new_str.join(my_string)

    print(my_string)

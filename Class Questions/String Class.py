# Task :
#
# Write a class that stores a string and all its status details including no. of
# Uppercase , lowercase character, vowels, consonants and spaces within the string.
# Display the Status details using display stack function.


class Alpha:

    upper_case = 0
    lower_case = 0
    vowel_count = 0
    consonent = 0
    spaces = 0

    def __init__(self,string):
        self.string = string

    def counter(self):
        length = len(string)

        vowels_list = ['a','e','i','o','u','A','E','I','O','U']
        space_list = [' ']

        for i in range(length):
            if(string[i].isupper()):
                Alpha.upper_case += 1

            if(string[i].islower()):
                Alpha.lower_case += 1

            if string[i] in vowels_list:
                Alpha.vowel_count += 1

            if string[i] in space_list:
                Alpha.spaces += 1

            if string[i] not in space_list and string[i] not in vowels_list:
                Alpha.consonent += 1

    def display(self):
        print(f'\n************************** RESULT **************************')
        print(f'Upper Case Letters : {Alpha.upper_case}')
        print(f'Lower Case Letters : {Alpha.lower_case}')
        print(f'Vowels : {Alpha.vowel_count}')
        print(f'Consonants : {Alpha.consonent}')
        print(f'Spaces : {Alpha.spaces}')
        print(f'************************************************************')


string = input('Enter a String : ')
my_obj = Alpha(string)
my_obj.counter()
my_obj.display()

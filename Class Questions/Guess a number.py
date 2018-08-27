# Task :
#
# Guess a number

import random

if __name__ == '__main__':
    my_list = [i for i in range(1,7)]
    n = 0
    ran_int = random.choice(my_list)

    while (n < 3):
        num = int(input('Enter Your Choice : '))

        if(num == ran_int):
            print('Yeah! Your guess is right')
            break
        else:
            print('Oops! Wrong Guess... TRY AGAIN')
            n += 1

            if(n == 2):
                print('Sorry! Max Guesses Reached')

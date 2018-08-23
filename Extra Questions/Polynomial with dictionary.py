# Task :
#
# W.A.P to evaluate one variable polynomial :
# f(x) = -2 + x**2 + 3*x**3       for x = 2
# using dictionary of coefficients of the polynomial

def polynomial(my_dict):
    sum = 0
    x = int(input('Enter X : '))
    for a,b in my_dict.items():
        sum = sum + b * x**a

    return(sum)

if __name__ == '__main__':
    my_dict = {}
    n = int(input('Enter Largest Power of X : '))

    for i in range(n+1):
        num = int(input(f"Enter Number for X's Power = {i} : "))
        my_dict[i] = num

    result = polynomial(my_dict)

    print(f'Result is : {result}')

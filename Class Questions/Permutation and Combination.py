def permutation(fact_n,fact_n_r):

    per = fact_n//fact_n_r
    return per

def combination(fact_n,fact_r,fact_n_r):

    com = fact_n//(fact_n_r *fact_r)
    return com


if __name__ == '__main__':
    n = int(input('Enter Value of n : '))
    r = int(input('Enter Value of r : '))

    fact_n = 1
    fact_r = 1
    n_r = n-r
    fact_n_r = 1

    for i in range(1,n+1):
        fact_n = fact_n * i

    for i in range(1,r+1):
        fact_r = fact_r * i

    for i in range(1,n_r+1):
        fact_n_r = fact_n_r * i

    p = permutation(fact_n,fact_n_r)
    c = combination(fact_n,fact_r,fact_n_r)

    print('Permutation :',p)
    print('Combination :',c)

def prime_no(num):
    if(num == 2):
        return True
    elif(num%2 == 0):
        return False
    else:
        for i in range(2,num):
            if(num%i == 0):
                return False
            else:
                return True

if __name__ == '__main__':
    my_list = list(range(1,100))

    is_prime = filter(prime_no,my_list)

    for i in is_prime:
        cal = i**i + 2
        print(cal,'\n')

def si(interest):
    p = int(input('Enter Principle : '))
    t = int(input('Enter Time : '))
    sim_int = (p * interest * t)//100
    return sim_int


if __name__ == '__main__':
    age = input('Enter Customer is Senior or not (Enter S for Senior) : ')
    age = age.lower()
    if(age == 's'):
        interest = 12
        simple_interest = si(interest)
        print('Simple Interest :',simple_interest)

    else:
        interest = 10
        simple_interest = si(interest)
        print('Simple Interest :',simple_interest)

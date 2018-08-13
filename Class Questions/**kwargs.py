def fun(**kwargs):
    print(kwargs)

str = input('Enter a String : ')

a = str.split()
key1 = a[0]
value = a[3]

fun(key1=value)

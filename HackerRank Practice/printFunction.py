# Read an integer N.
#
# Without using any string methods, try to print the following:
# 123 ... N
#
# Note that "..." represents the values in between.


if __name__ == '__main__':
    n = int(input())

    for i in range(n+1):
        if(i!=0):
            print(i,end="")

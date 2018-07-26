# Task
# Read an integer N. For all non-negative integers i<N, print i^2.

n = int(input())
my_list = list(range(0,21))

for num in my_list:
    if(num<n):
        sq = num * num
        print(sq)

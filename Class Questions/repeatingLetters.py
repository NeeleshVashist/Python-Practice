st = input('Enter a String : ')
count = 0
my_dic = {}

for i in range(len(st)):
    for j in range(len(st)):
        if(st[i] == st[j]):
            count += 1

    my_dic[st[i]] = count
    count = 0

print('Dictionary is :',my_dic)

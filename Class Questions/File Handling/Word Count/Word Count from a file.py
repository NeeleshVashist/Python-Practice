# Task :
#
# Count the Number of words in a file

file=open('my_file.txt','r+')
wordcount={}
a=0
for word in file.read().split():
    if word not in  wordcount:
        wordcount[word]=1
        a=a+1
    else:
        wordcount[word] +=1
        a=a+1
print(f'Word Count Dictionary :\n{wordcount}')
print('Total Words: ',a)
file.close()

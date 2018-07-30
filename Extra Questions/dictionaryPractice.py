# Create two dictionaries
# First Dictionary : English(Key) -> Hindi(Value)
# Second Dictionary : Hindi(Key) -> Punjabi(Value)
#
# Sample Output : English : Hindi : Punjabi

first_dic = {'Walk' : 'Chalna', 'Kid' : 'Baccha'}
second_dic = {'Chalna' : 'Turna', 'Baccha' : 'Niyana'}

print('English' + '\t || \t' + 'Hindi' + '\t || \t' + 'Punjabi')
print('***************************************')
for a,b in first_dic.items():
    for x,y in second_dic.items():
        if(b == x):
            print(a + '\t -> \t' + b + '\t -> \t' + y)

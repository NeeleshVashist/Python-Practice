import palindrome

str = input("Enter a String : ")
x = palindrome.pal(str)
if(x == True):
    print("It is palindrome")
else:
    print("It is not palindrome")

# Task :
#
# If word starts with a vowel, add 'ay' to end
# If word does not start with a vowel, put first letter at the end, then add 'ay'
#
# Example :
# word --> ordway
# apple --> appleay

def pig_latin(word):

    first_letter = word[0]

    # Check if word is vowel

    if first_letter in 'aeiou':
        pig_word = word + 'ay'

    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

if __name__ == '__main__':

    word = input('Enter a String : ')
    final_word = pig_latin(word)

    print('Required String :',final_word)

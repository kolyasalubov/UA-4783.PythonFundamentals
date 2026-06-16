'''
Task3. Write a function that calculates the number of characters included in given string
'''

def num_of_characters(word):
    used_letters = []
    letter_dict = {}
    for i in word:
        if i not in used_letters:
            letter_dict[i] = word.count(i)
            used_letters.append(i)
    
    return letter_dict

word = input('Enter your word: ')
print(num_of_characters(word))

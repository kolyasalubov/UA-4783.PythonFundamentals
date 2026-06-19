word = input("Введіть ваше слово: ")

def calc_char(word):
    d = {}
    for char in word:
        if char in d:
            d[char] += 1
        else: 
            d[char] = 1
    return d
print(calc_char(word))
import re
password = input()

low_letters = re.search(r'[a-z]+', password)
up_letters = re.search(r'[A-Z]+', password)
digits = re.search(r'[0-9]+', password)
specials = re.search(r'[$@#]', password)

if 6 <= len(password) <= 16 and low_letters and up_letters and digits and specials:
    print('Пароль підходить')
else:
    print('Пароль не підходить')

import re
password = input()

low_text = re.search("[a-z]", password)
upper_text = re.search("[A-Z]", password)
numbers = re.search("[0-9]", password)
specialist = re.search("[@$#]", password)

if 6<=len(password)<=16 and low_text and upper_text and numbers and specialist:
    print("Password correct")
else:
    print("Passworn not correct")
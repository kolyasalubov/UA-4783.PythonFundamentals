# Write a Python program to check the validity of a password (input from users).
# Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = input("Print your password: ")
low = False
up = False
digit = False
specsim = False
for i in password:
    if i.islower():
        low = True
    elif i.isupper():
        up = True
    elif i.isdigit():
        digit = True
    elif i in ['$', "#", "@"]:
        specsim = True
    else:
        print("Incorrect password")
if len(password) < 6 or len(password) > 16:
    print("Your password is very small or long")
elif low and up and digit and specsim == True:
        print(f"Your password is correct {password}")
else:
    print("Incorrect password")
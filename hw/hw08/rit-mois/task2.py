password = input("Enter password: ")

lower = upper = digit = special = False

for ch in password:
    if ch.islower():
        lower = True
    elif ch.isupper():
        upper = True
    elif ch.isdigit():
        digit = True
    elif ch in "$#@":
        special = True

if (6 <= len(password) <= 16 and
        lower and upper and digit and special):
    print("Valid Password")
else:
    print("Invalid Password")

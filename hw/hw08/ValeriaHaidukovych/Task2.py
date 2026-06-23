import re

password = input()
if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$", password):
    print("Your password is valid")
else:
    print("Your password is invalid")

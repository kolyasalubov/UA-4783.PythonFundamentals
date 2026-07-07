import re
password = input("Enter your new password: ")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"

if re.fullmatch(pattern, password):
    print("Password accepted")
else:
    print("Invalid password")
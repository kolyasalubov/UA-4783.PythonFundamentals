import re

user_password = input("Enter your password: ")

if re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$", user_password):
    print("\nPassword is valid.")
else:
    print("\nPassword is invalid.")
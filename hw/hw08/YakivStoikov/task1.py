import re

password = input()

def validate_password(password: str) -> None:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).{6,16}$'
    if re.match(pattern, password):
        print("Valid password")
    else:
        print("Invalid password. Must be 6-16 chars with an uppercase, lowercase, digit, and [@#$].")

validate_password(password)

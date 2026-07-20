import re


def validate_password(password):
    valid = re.findall(r'[a-z][A-Z][1-9][^0-9]', password)
    return valid

password = input("Enter ur password: ")
print(validate_password(password))
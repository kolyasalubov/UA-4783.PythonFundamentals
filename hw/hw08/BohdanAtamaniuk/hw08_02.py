import re


def validate_password(password):
    if 6 <= len(password) <= 16:
        if re.search(r'[a-z]', password) != None:
            if re.search(r'[A-Z]', password) != None:
                if re.search(r'\d', password) != None: 
                    if re.search(r'[$#@]', password):
                        return ("Ur password is saved")
                    else:
                        return("Ur password is unvalid")
                else:
                    return("Ur password is unvalid")
            else:
                return("Ur password is unvalid")
        else:
            return("Ur password is unvalid")
    else:
        return("Ur password is unvalid")

password = input('''(Ur password may be:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.)
Enter ur password: ''')
print(validate_password(password))
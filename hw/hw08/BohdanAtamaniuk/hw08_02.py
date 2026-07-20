import re


def validate_password(password):
    if 6 < len(password) < 16:
        if re.search(r'[a-z]', password) != None:
            if re.search(r'[A_Z]', password) != None:
                if re.search(r'\d', password) != None: 
                    if re.search(r'^[0-9]', password):
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

password = input("Enter ur password: ")
print(validate_password(password))
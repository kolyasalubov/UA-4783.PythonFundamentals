def validate(password):
    if len(password) < 6 or len(password) > 16:
        return False
        
    if not any(char.islower() for char in password):
        return False
        
    if not any(char.isupper() for char in password):
        return False
        
    if not any(char.isdigit() for char in password):
        return False

    special_chars = "$#@"
    if not any(char in special_chars for char in password):
        return False
        
    return True


print(validate(input("Enter your password for validation\n")))

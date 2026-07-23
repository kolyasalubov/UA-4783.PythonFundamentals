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
    else: print("Incorrect password") 
if len(password) < 6 or len(password) > 16: 
    print("Your password is very small or long") 
elif low == True and up == True and digit == True and specsim == True: 
        print(f"Your password is correct {password}")
else:
     print("Incorrect password") 
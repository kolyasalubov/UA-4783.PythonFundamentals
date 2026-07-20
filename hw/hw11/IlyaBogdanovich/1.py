age = input("Please enter your age: ")

def check(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError
        if age % 2 == 0:
            return "Your age number is even"
        else:
            return "Your age number is odd"
    except ValueError, TypeError:
        return "Wrong input data!"
    

print(check(age))

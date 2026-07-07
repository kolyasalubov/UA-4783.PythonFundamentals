
def your_age(num):
    age = int(num)
    if age > 0:
        if int(age) % 2 == 0:
            return "Your age is even"
        elif int(age) % 2 != 0:
            return "Your age is odd"
    else:
        raise Exception(f"Error, {age} is incorrect")
    
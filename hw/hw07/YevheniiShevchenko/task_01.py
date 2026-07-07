def largest_number(x,y):
    """The function return the largest number among two"""
    if x == y:
        return "Numbers are equal"
    elif x > y:
        return f"{x} is the largest number"
    else:
        return f"{y} is the largest number"

print(largest_number(3,2))
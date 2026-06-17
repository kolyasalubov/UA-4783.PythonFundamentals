def bigger_num(num1: int, num2: int):
    """Return the largest number"""
    if num1 > num2:
        result = num1
    elif num1 < num2:
        result = num2
    else:
        result = "Числа рівні"
    return result

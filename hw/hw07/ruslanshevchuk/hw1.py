def my_func(x,y):
    """Ця функція повертає більше число"""
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Числа однакові"

result = my_func(5, 7)
print(result)
def larg_number(x,y):
    """
    Ця функція визначає, яке з двох вказаних чисел є більшим
    
    Аргументи:
    x(int) - перше число
    y(int) - друге число
    
    Повертає:
    int: Число x або число y
    """
    if x > y:
        return x
    else:
        return y
print(larg_number(3,14 , 5,15))
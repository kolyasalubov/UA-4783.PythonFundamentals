def larg_number(x,y) -> float:
    """
    Ця функція визначає, яке з двох вказаних чисел є більшим
    
    Аргументи:
    x(int, float)
    y(int, float)
    
    
    """
    if x > y:
        return x
    else:
        return y
print(larg_number(3,14 , 5,15))
def greater_number(x,y):
    '''The function returns one of the two numbers, the larger one.'''
    if x == y:
        return "The numbers are equal"
    elif x > y:
        return x
    else:
        return y

print(greater_number(20, 10))


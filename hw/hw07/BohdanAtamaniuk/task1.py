def largest(a, b):
    '''
    Function returns the largest of two numbers.
    :param a: first number
    :param b: second number
    '''
    if a > b:
        return a
    else:
        return b
    
fist_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print("The largest number is:", largest(fist_number, second_number))

def greater_number():
    '''The function returns one of the two numbers entered—specifically, the larger one.'''
    try:
        a = int(input("Please enter a first number: "))
        b = int(input("Please enter a second number: "))
        if a == b:
            return "Numbers equal"
        else:
            return a if a > b else b
    except ValueError:
        return "Invalid input, please enter a number"

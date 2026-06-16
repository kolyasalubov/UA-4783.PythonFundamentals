'''Task1 Write a function that returns the largest number of two numbers'''
def largest_number(a, b):
    if a > b:
        return a
    return b

a = float(input('Frist number = '))
b = float(input('Second number = '))

print(f'The largest number = {largest_number(a, b)}')

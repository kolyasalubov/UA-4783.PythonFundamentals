def check_age(age):
    if age < 0:
        raise ValueError('The. age can not be negative')
    return 'even' if age % 2 == 0 else 'odd'

try:
    age = int(input('Enter the age\n'))
    print(check_age(age))
except ValueError as e:
    if 'invalid literal' in str(e):
        print('Input the number')
    else:
        print(e)

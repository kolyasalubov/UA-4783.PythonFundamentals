days = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

try:
    day = int(input('Enter the number between 1 to 7\n'))
    print(days[day])
except ValueError:
    print('The value should be an integer')
except KeyError:
    print('The value must be in in the range from 1 to 7')

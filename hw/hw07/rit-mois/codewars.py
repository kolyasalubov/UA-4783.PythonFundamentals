# I Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# II Find The Distance Between Two Points
import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)


# III No yelling!
def filter_words(st):
    return ' '.join(st.capitalize().split())


# IV Convert a Number to a String!
def number_to_string(num):
    return str(num)


# V Reversing Words in a String
def reverse(st):
    return ' '.join(st.split(' ')[::-1])


# VI Reverse List Order
def reverse_list(l):
    return l[::-1]


# VII Multiples of 3 or 5
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


# VIII Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# IX Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"


# X Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI Counting sheep...
def count_sheep(sheep):
    return sheep.count(True)


# XII Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False

'''I. Jenny's secret message'''
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

'''II. Find The Distance Between Two Points'''
# def distance(x1, y1, x2, y2):
#     return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

'''No yelling!'''
# def filter_words(st):
#     return ' '.join(st.split()).capitalize()

'''Convert a Number to a String!'''
# def number_to_string(num):
#     return str(num)

'''Reversing Words in a String'''
# def reverse(st):
#     st = st.split()[::-1]
#     return ' '.join(st)

'''Reverse List Order'''
# def reverse_list(l):
#     return l[::-1]

'''Multiples of 3 or 5'''
# def solution(number):
#     sum = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum

'''Will you make it?'''
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump <= (mpg * fuel_left):
#         return True
#     return False

'''Are You Playing Banjo?'''
# def are_you_playing_banjo(name):
#     if name.lower().strip()[0] == 'r':
#         return f'{name} plays banjo'
#     return f'{name} does not play banjo'

'''Convert boolean values to strings 'Yes' or 'No'.'''
# def bool_to_word(boolean):
#     return 'Yes' if boolean == True else 'No'

'''Counting sheep...'''
# def count_sheeps(sheep):
#     return sheep.count(True)

'''Is this my tail?'''
# def correct_tail(body, tail):
#     last = body[-1]
#     if last == tail:
#         return True
#     else:
#         return False
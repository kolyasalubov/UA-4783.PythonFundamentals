# Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)

######################################################

# Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     return round(((x2 - x1 ) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)

######################################################

#No yelling!

# def filter_words(st):
#     return " ".join(st.split()).lower().capitalize()

######################################################

#Convert a Number to a String!
# def number_to_string(num):
#     return f"{num}"

######################################################

# Reversing Words in a String

# First version:
# def reverse(st):
#     words = st.strip().split()
#     reversed_seq = words[::-1]
#     joined = " ".join(reversed)
#     return joined
# Second version:
# def reverse(st):
#     return " ".join(st.split()[::-1])

######################################################

# Multiples of 3 or 5

# def solution(number):
#     if number < 0:
#         return 0
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total

######################################################

# Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return fuel_left * mpg >= distance_to_pump

######################################################

# Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     return f"{name} plays banjo" if name.casefold()[0] == "r" else f"{name} does not play banjo"

######################################################

# Convert boolean values to strings 'Yes' or 'No'
# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"

######################################################

# Counting sheep
# def count_sheeps(sheep):
#     count = 0
#     for value in sheep:
#         if value:
#             count += 1
#     return count

######################################################

# Is this my tail?
# def correct_tail(body, tail):
#     return body[-1] == tail
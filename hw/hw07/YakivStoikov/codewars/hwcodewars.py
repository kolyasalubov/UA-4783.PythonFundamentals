# Jenny's secret message
# 
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)
# 
# =========================================================
# 
# Simple: Find The Distance Between Two Points
# 
# def distance(x1, y1, x2, y2):
#     return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
# 
# ========================================================
# 
# No yelling!
# 
# def filter_words(st):
#     st = st.lower()
#     st = st.capitalize()
#     st = " ".join(st.split())
#     return st
# 
# ========================================================
# 
# Convert a Number to a String!
# 
# def number_to_string(num):
#     return str(num)
# 
# =======================================================
# 
# Reversing Words in a String
# 
# def reverse(st):
#     return " ".join(st.split()[::-1])
# 
# =======================================================
# 
# Reverse List Order
# 
# def reverse_list(l):
#     return l[::-1]
# 
# =======================================================
# 
# Multiples of 3 or 5
# 
# def solution(number):
#     total = 0
#     for i in range(1, number):
#          if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total
# 
# =======================================================
# 
# Will you make it?
# 
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left
# 
# ======================================================
# 
# Are You Playing Banjo?
#
# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
# 
# ======================================================
#
# Convert boolean values to strings 'Yes' or 'No'.
# 
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
# 
# ======================================================
# 
# Counting sheep...
# 
# def count_sheeps(sheep):
#     sheeps_count = 0
#     for sheep in sheep:
#         if sheep:
#             sheeps_count += 1
#     return sheeps_count
# 
# =====================================================
# 
# Is this my tail?
# 
# def correct_tail(body, tail):
#     sub = body[-1]
#     if sub == tail:
#         return True
#     else:
#         return False
